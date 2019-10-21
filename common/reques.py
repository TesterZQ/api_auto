
'''请求类'''

import requests
from common.config import Readconfig

class Request:
    '''封装请求方式'''

    def __init__(self,methon,url,data = None,cookies = None,headers = None):
        try:
            get_url = Readconfig().get(section='api', option='url_pse')
            url = get_url + url
            if methon == 'get':
                self.resp = requests.get(url=url,params=data,cookies = cookies,headers = headers)
            elif methon =='post':
                self.resp = requests.post(url=url,params=data,cookies = cookies,headers = headers)
        except Exception as e:
            print('请求方式错误，请检查')
            raise e

    def get_status_code(self):
        '''#返回请求状态'''
        return self.resp.status_code

    def get_text(self):
        '''返回响应体'''
        return self.resp.text

    def get_json(self):
        '''#返回响应正文'''
        return self.resp.json()

    def get_cookies(self,key):#封装，返回cookie
        if key is not None:
            return self.resp.cookies[key]
        else:
            return self.resp.cookies  #返回cookie对象


