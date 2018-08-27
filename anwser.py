#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json
from config import *



def buildHeader():
    curTime = str(int(time.time()))
    param = "{\"result_level\":\""+RESULT_LEVEL+"\",\"auth_id\":\""+AUTH_ID+"\",\"data_type\":\""+DATA_TYPE+"\",\"sample_rate\":\""+SAMPLE_RATE+"\",\"scene\":\""+SCENE+"\",\"lat\":\""+LAT+"\",\"lng\":\""+LNG+"\"}"
    #使用个性化参数时参数格式如下：
    #param = "{\"result_level\":\""+RESULT_LEVEL+"\",\"auth_id\":\""+AUTH_ID+"\",\"data_type\":\""+DATA_TYPE+"\",\"sample_rate\":\""+SAMPLE_RATE+"\",\"scene\":\""+SCENE+"\",\"lat\":\""+LAT+"\",\"lng\":\""+LNG+"\",\"pers_param\":\""+PERS_PARAM+"\"}"
    param_byte = param.encode()
    paramBase64 = base64.b64encode(param_byte)

    m2 = hashlib.md5()
    aa = API_KEY + curTime + paramBase64.decode('utf-8')
    m2.update(aa.encode())
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID2,
        'X-CheckSum': checkSum,
    }
    return header


def anwser(data):
    r = requests.post(URL, headers=buildHeader(), data=data)
    ret = json.loads(r.content)
    return ret

if __name__ == '__main__':
    with open(FILE_PATH, 'rb') as f:
        file_content = f.read()
    anwser(file_content)