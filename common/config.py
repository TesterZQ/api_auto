'''
配置文件读取
'''
import os
import configparser
from common import contants
import os

class Readconfig:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        # 加载配置文件。配置文件的绝对路径
        file_name = os.path.join(contants.file_path, 'globla.conf')
        #读取配置文件
        self.cf.read(filenames=file_name)
        #判断配置文件，如果为True执行，再次读取test_data_conf.conf配置文件，如果flase读取第二个配置文件
        if self.getboolean_1('swtich','on'):
            test_data_conf = os.path.join(contants.file_path, 'test_data_conf.conf')
            # 读取配置文件
            self.cf.read(filenames=test_data_conf)
        else:
            test_data_conf2 = os.path.join(contants.file_path, 'test_data_conf2.conf')
            # 读取配置文件
            self.cf.read(filenames=test_data_conf2)


    def get(self,section,option):
        '''通过get方法拿到配置文件内的section,option'''
        return self.cf.get(section,option)


    def getboolean_1(self,section,option):
        return self.cf.getboolean(section,option)


if __name__ == '__main__':
    rf = Readconfig()
    a=rf.get('api','url_pse')
    print(a)