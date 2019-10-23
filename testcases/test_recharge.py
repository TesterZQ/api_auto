import unittest
from common.do_excel import DoExcel
from common import contants
from common.reques import Request
from ddt import ddt,data,unpack
from common.basic_data import DoRegex,Context
import json


#打开表格
do_excel = DoExcel(contants.case_file1)
#定位表单
cases = do_excel.get_cases('recharge')

@ddt
class TestRecharge(unittest.TestCase):

    def setUp(self):
        print('测试数据准备')

    #使用ddt把表单内的全部数据取出
    @data(*cases)
    def test_rechargen(self,case):
        #参数化处理
        test_data=DoRegex.replace(case.data)#通过正则获取表格内的目标字符串
        test_data = json.loads(test_data)#把目标字符串转化为字典
        if hasattr(Context,'cookies'):
            cookies = getattr(Context,'cookies')
        else:
            cookies=None
        resp = Request(methon=case.method, url=case.url, data=test_data,cookies=cookies)  # 通过封装Request类来完成接口的调用
        # 判断有没有cookie
        if resp.get_cookies():
            setattr(Context,'cookies',resp.get_cookies())
        resp_dict = resp.get_json()
        print(resp_dict)
        # #断言表格内的期望结果与接口内实际返回的结果
        self.assertEqual(case.expected,int(resp_dict['code']))
    def tearDown(self):
        print('测试清除')


