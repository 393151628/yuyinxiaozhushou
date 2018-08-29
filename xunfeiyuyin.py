#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib
from urllib import request
import json
import hashlib
import base64
import json
from config import *
from anwser import anwser

def create_header(param, api_key):
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode())
    x_time = int(int(round(time.time() * 1000)) / 1000)
    aa = api_key + str(x_time) + x_param.decode('utf-8')
    x_checksum = hashlib.md5(aa.encode()).hexdigest()
    x_header = {'X-Appid': APPID1,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum
                }
    return x_header


def video2text(file_content):
    base64_audio = base64.b64encode(file_content)
    body = urllib.parse.urlencode({'audio': base64_audio})
    url = 'http://api.xfyun.cn/v1/service/v1/iat'
    param = {"engine_type": "sms16k", "aue": "raw"}

    x_header = create_header(param, video2text_api_key)

    req = request.Request(url, body.encode(), x_header)
    result = request.urlopen(req)
    result = result.read()
    data = json.loads(result.decode('utf-8'))
    if data.get('code') == '0' and data.get('desc') == 'success':
        return data['data']
    else:
        return None


def words_analysis(words, action):
    body = urllib.parse.urlencode({'text': words}).encode('utf-8')
    # 中文分词(cws)、词性标注(pos)、依存句法分析(dp)、命名实体识别(ner)、语义角色标注(srl)、语义依存分析(sdp)
    url = 'http://ltpapi.xfyun.cn/v1/%s' % action
    param = {"type": "dependent"}

    x_header = create_header(param, words_api_key)
    req = request.Request(url, body, x_header)
    result = request.urlopen(req)
    result = result.read()
    data = json.loads(result.decode('utf-8'))
    return data


def analysis_main(data):
    cws_list = data['cws']['data']['word']
    dp_list = data['dp']['data']['dp']
    ner_list = data['ner']['data']['ner']
    pos_list = data['pos']['data']['pos']
    sdp_list = data['sdp']['data']['sdp']
    srl_list = data['srl']['data']
    # print('cws_list:', cws_list)
    # print('dp_list:', dp_list)
    # print('pos:', pos_list)
    # print('ner:', ner_list)
    # print('sdp:', sdp_list)
    # print('srl:', srl_list)
    # print(data)
    for idx, _dp in enumerate(dp_list):
        a = cws_list[idx]
        sdp = sdp_list[idx]
        if _dp['parent'] < 0:
            b = ' '
        else:
            b = cws_list[_dp['parent']]

        sdp_idx = sdp['parent'] - 1
        if sdp_idx < 0:
            c = ''
        else:
            c = cws_list[sdp_idx]

        print(a, '-------->', b, '[', DP_DICT[_dp['relate']][0], ']', '==============>', c, '[', SDP_DICT[sdp['relate']], ']')

    if analysis_excuse(cws_list, dp_list, ner_list, pos_list):
        return 'excute_order'
    if analysis_phone(cws_list, dp_list, ner_list, pos_list):
        return 'toon://siri/callPhone?params={"tel":"0591-88610313"}'
    return False

def analysis_excuse(cws_list, dp_list, ner_list, pos_list):
    excuese_idx_list = []
    for idx, words in enumerate(cws_list):
        if words in EXCUSEORDER:
            excuese_idx_list.append(idx)

    if excuese_idx_list:
        for idx in excuese_idx_list:
            dp = dp_list[idx]
            # 关键词是动宾关系
            if dp['relate'] == 'VOB':
                for ner in ner_list:
                    if ner != '0':
                        return True
            # 关键词是核心关系 且 为动词
            if dp['relate'] == 'HED' and pos_list[idx] == 'v':
                return True
    else:
        return False

def analysis_phone(cws_list, dp_list, ner_list, pos_list):
    phone_idx_list = []
    # 把分词中存在查找电话的关键字存个列表
    for idx, words in enumerate(cws_list):
        if words in PHONENUMBER:
            phone_idx_list.append(idx)
    if phone_idx_list:
        for idx, dp in enumerate(dp_list):
            # 在指向电话关键字的关系为 定中关系的词  如果是个 地名 人名 机构名 或者 符合一个名词标准 既认为查找这个电话
            if dp['parent'] in phone_idx_list and dp['relate'] == 'ATT' and \
                    (ner_list[idx] != '0' or pos_list[idx].startswith('n')):
                print('n:', cws_list[idx])
                print('phonekeywords:', cws_list[dp['parent']])
                # goto_tmail()
                return True
    else:
        return False


def goto_tmail():
    return


def main(file_content):
    # with open(FILE_PATH, 'rb') as f:
    #     file_content = f.read()
    words = video2text(file_content)
    if words:
        # words = '打电话给赵国庆'
        # words = '我想请问今天北京天气如何。'
        data = {}
        for i in action_list:
            ret = words_analysis(words, i)
            data[i] = ret
        ret = analysis_main(data)
        data = {
            'code': 0,  # 0为成功  1为失败
            'message': '',  # 展示信息
            'action': '',  # tmail or  toon的 跳转 协议
            'type': 1,  # 0为展示信息， 1为 tmail or toon的跳转
        }
        if ret:
            print(ret)
            data['type'] = 1
            data['action'] = ret
            return data
        else:
            data['type'] = 0
            r = anwser(file_content)
            if r['code'] == '0':
                for i in r['data']:
                    if i.get('intent', {}).get('answer', {}).get('text'):
                        ans = i['intent']['answer']['text']
                        print(ans)
                        data['message'] = ans
                        break
                else:
                    data['message'] = '我听不懂'
            else:
                data['message'] = '我听不懂'
            return data
    else:
        return False


if __name__ == '__main__':
    main()
    # w = ''
    # ret = words_analysis()
