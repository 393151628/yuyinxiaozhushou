# -*- coding: utf-8 -*-

import os
import datetime
import uuid

import tornado.options
from tornado.web import RequestHandler
from tornado.options import define, options
from tornado.escape import json_decode, json_encode


# detector = MTCNN()
# 比检测位置向外扩一些
from xunfeiyuyin import main

define("port", default=8001, type=int)

UPLOAD_PATH = r'/opt/yuyinxiaozhushou/tmp'
class FileUploadHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', '*')
    def get(self):
        self.write('''
<html>
  <head><title>Upload File</title></head>
  <body>
    <form action='/api/upload' enctype="multipart/form-data" method='post'>
    <input type='file' name='file'/><br/>
    <input type='submit' value='submit'/>
    </form>
  </body>
</html>
''')

    def post(self):
        file_metas = self.request.files.get('file', None)  # 提取表单中‘name’为‘file’的文件元数据

        if not file_metas:
            data = {
                'code': 1,  # 0为成功  1为失败
                'message': '上传失败',  # 展示信息
                'action': '',  # tmail or  toon的 跳转 协议
                'type': 0,  # 0为展示信息， 1为 tmail or toon的跳转
            }
            self.write(json_encode(data))
            self.finish()

        for meta in file_metas:
            # filename = meta['filename']
            # t = datetime.datetime.now().strftime('%Y%m%d%H%M')
            # uid = str(uuid.uuid1())
            # upload_path = os.path.join(UPLOAD_PATH, uid + '_' + t + '_' + filename)
            # # file_path = os.path.join(upload_path, filename)
            # with open(upload_path, 'wb') as up:
            #     up.write(meta['body'])
                # OR do other thing
            # ret.append(upload_path)
            data = main(meta['body'])
        self.write(json_encode(data))
        self.finish()


app = tornado.web.Application([
    (r"/api/upload", FileUploadHandler),
],
    debug=True
)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
