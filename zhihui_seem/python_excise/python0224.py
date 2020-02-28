# import  py_compile
# py_compile.compile("excise.py")



##赋值练习
'''
# a =1
# print(a)
# print(type(a))
#
#
# b=123
# b=234
# print(b)
#
# world="i love you 1314"
# print(world)
#
# daysperweek=7
# hoursperday=24
# minterperhour=60
# print(daysperweek*hoursperday*minterperhour)
#
# hoursperday=27
# print(daysperweek*hoursperday*minterperhour)
#
#
# a=23
# print(~a)
'''

###运算符表达式练习:方法一


'''
# action={"+","-","*","/"}
# do=input("输入运算符号")
# a=int(input())
# b=int(input())
# if do=="+":
#     print(a+b)
# elif  do=="-":
#     print(a-b)
# elif  do=="*":
#     print(a*b)
# else:
#     print(a/b)
'''

###运算符表达式练习:方法二
'''
def count(L):
    if L=="+":
        c=a+b
    elif  L=="-":
        c=(a-b)
    elif  L=="*":
        c=(a*b)
    elif L=="/":
        c=(a/b)
    else:
        c=("错啦")

    print("{}{}{}={}".format(a,L,b,c))
if __name__=="__main__":
    a=int(input())
    b = int(input())
    count("+")
'''


###运算符表达式练习
'''
people=3
free=15
total=35.27
per_people=(free+total)/people
print("每个人付{}".format(per_people))

a=12.5
b=16.7
c=(a+b)*2
s=a*b
print("周长为{}".format(c),"面积为{}".format(s))


F=int(input("输入摄氏温度："))
C=5/9*(F-32)
print("华氏温度为{}".format(C))

'''


#字典
# ddict={}.fromkeys(('x','y'),-1)
# print(ddict)

# s={1:"123",2:"3434",4:"ere"}
# for i in s.items():
#     print(i)
# for a,b in s.items():
#     print(a,b)

##5*4#3
'''
from functools import reduce
l={1,2,3,4,5}
def f(x,y):
    return x*y
print(reduce(f,l))
'''


'''
from __future__ import division
def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y

def operater(x,o,y):
    if o=="+":
        jia(x,y)
    elif o=="-":
        jian(x,y)
    elif o=="*":
        cheng(x,y)
    else:
        chu()
if __name__=="__main__":
    print(operater(3,'-',1))
'''

name=["zhangsan","lisi","xiaowang"]
age=[12,11]
# a=(zip(name,age))
# for i in a :
#     print(i)
b=(map(name,age))
for j in b:
    print(j)