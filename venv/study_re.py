'''

正则表达式：是对字符串操作的一种逻辑公式
完成字符串的查找
'''

import re

#()z在正则表达式内是组的概念
# s  =  '{"mobilephone":"15810447656","pwd":"123456"}'#目标数据库

# s1 = 'hello word,hello'
# s2 ='hello'
#
# res=re.match(pattern=s2,string=s1)#从最开始的位置找
# # re.search()#从任意位置找字符串
# res_2=re.findall(pattern=s2,string=s1)#查找全部匹配字符串，并且返回
# print(res_2)


# s  =  '{"mobilephone":"15810447656","pwd":"123456"}'
# res=re.findall(pattern='(\d{11})',string=s)
# print(res)
# moblilephone = res[0]
# print(moblilephone)
# ss=s.replace(moblilephone,'15810447656')#返回到目标文件
# print(ss)


s = '{"mobilephone":"${register}","pwd":"123456"}'
res=re.search(pattern='\$\{(.*?)\}',string=s)
print(res)
# print(res.group(0),res.group(5))
res1 = re.sub('\$\{(.*?)\}','12345',s)
print(res1)


