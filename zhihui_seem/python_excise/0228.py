import re
'''
s=r'abc'
print(re.findall(s,"aaaaaaa"))
print(re.findall(s,"abc"))

#单个匹配
s="top tip silp"
res=r'tip'
print(re.findall(res,s))

#多个匹配
s="top tip silp"
res=r"t[io]p"
print(re.findall(res,s))



#多个匹配且取反
# st="top tip tqp twp tep"
st="top tip slp map eee"
res = r"t[^io]p"
print(re.findall(res,st))
'''

s="hello word,hello boy"
r=r"hello"
print(re.findall(s,r))


r1=r"boy$"
print(re.findall(s,r1))