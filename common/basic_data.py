'''
测试上下文，做正则处理

'''
import re
class DoRegex:
    '''正则表达式封装'''
    @staticmethod
    def replace(target):#正则查找数据并且替换
        '''target目标字符串，表格内有正则标识的字符串'''
        pattern = '\$\{(.*?)\}'
        while re.search(pattern,target): #（循环条件：使用正则表达式，查找目标字符串）找到一个目标字符串就返回，此正则内有两个目标字符串，故此找到两个目标字符串
            m = re.search(pattern,target)
            key = m.group(1) #取第一个分组内的字符
            from common.basic_data import  Context
            user = getattr(Context,key)
            target = re.sub(pattern,user,target,count=1)
        return target


from common.config import Readconfig

class Context:
    config=Readconfig()
    #获取配置文件内的手机号与密码
    normal_user = config.get('basic','normal_user')
    pwd = config.get('basic','pwd')
    # print(normal_user,pwd)








'''
反射机制：
1.可以通过类.类变量取到类变量的值
2.能够没有对象的时候获取这个对象信息，甚至可以更改这个对象



getattr()获取变量的值
normal_user= getattr(Context,'normal_user')#
setattr()增加一个属性
setattr(Context,'admin_user','adc',)
delattr()删除一个属性
delattr(Context,'admin_user')
'''

if __name__ == '__main__':
    normal_user= getattr(Context,'normal_user')#
    print(normal_user)
    setattr(Context,'admin_user','adc',)
    delattr(Context,'admin_user')


