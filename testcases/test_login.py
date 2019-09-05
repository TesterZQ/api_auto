import unittest
from common.do_excel import DoExcel
from common import contants
from common.reques import Request
from ddt import ddt,data,unpack
import json

#打开表格
do_excel = DoExcel(contants.case_file)
#定位表单
cases = do_excel.get_cases('login')
@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        print('测试数据准备')
    #使用ddt把表单内的全部数据取出
    @data(*cases)
    def test_login(self,case):
        # #遍历表单内login内的测试数据
        # for case in cases:
            #把data转换成json格式
            # data = json.loads(case.data,encoding='utf-8')
            # print(data)
            #请求表单内数据
        resp = Request(methon=case.method, url=case.url, data=eval(case.data))  # 通过封装Request类来完成接口的调用
        print('status_code',resp.get_status_code())  # 打印响应码
        print(resp.get_text())
        #断言表格内的期望结果与接口内实际返回的结果
        self.assertEqual(case.expected,resp.get_text())
    def tearDown(self):
        print('测试清除')