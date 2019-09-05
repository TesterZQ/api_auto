'''配置文件路径获取'''
import os

file_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#os.path.abspath返回当前文件的绝对路径，os.path.dirname在绝对路径的基础上再次返回上一级目录
print(file_dir)
file_path = os.path.join(file_dir,'conf')#configs文件夹路径
print(file_path)



datas_dir = os.path.join(file_dir,'datas')#datas文件夹路径
#通过路径拼接获取datas文件夹下的api.xlsx文件路径，供测试用例内调用
case_file = os.path.join(datas_dir,'api.xlsx')
print(case_file)
report_dir = os.path.join(file_dir,'report')#report文件夹路径

logs_dir = os.path.join(file_dir,'logs')#logs文件夹路径