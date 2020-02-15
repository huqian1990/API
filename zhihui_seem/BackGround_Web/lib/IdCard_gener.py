import random
import random,string
# n=int(input('请输入生成随机密码的个数n=') )   # n=10
# m=int(input("请输入生成随机密码的长度m="))        # m=8


##随机生成身份证号
def IdCard_gener():
    num = string.digits+string.digits  # 生成['a',...,'z','A',...,'Z','0',...'9']
    new_chars = ' '.join(num)
    ll = new_chars.split()
    num = 0
    while num < 1:
        random.shuffle(ll)
        list1 = ll[:18]
        num += 1
        return (''.join(list1))

#随机生成电话号吗
def PhoneNum_gener():
    num = string.digits  # 生成['a',...,'z','A',...,'Z','0',...'9']
    new_chars = ' '.join(num)
    ll = new_chars.split()
    num = 0
    while num < 1:
        random.shuffle(ll)
        list1 = ll[:10]
        num += 1
        return (''.join(list1))

#随机生成车牌号码
def Carcode_gener():
    num=string.digits
    new_chars = ' '.join(num)
    ll = new_chars.split()
    num = 0
    while num < 1:
        random.shuffle(ll)
        list1 = ll[:5]
        num += 1
        return (''.join(list1))
if __name__=="__main__":
    print(IdCard_gener())
    print(PhoneNum_gener())
    print(Carcode_gener())







'''
========实际代码========
     import random, string

     n = int(input('请输入生成随机密码的个数n='))  # n=10
     m = int(input("请输入生成随机密码的长度m="))  # m=8
     chars = string.ascii_letters + string.digits  # 生成['a',...,'z','A',...,'Z','0',...'9']
     new_chars = ' '.join(chars)
     ll = new_chars.split()
     num = 0
     while num < n:
         random.shuffle(ll)
         list1 = ll[:m]
         num += 1
         print(''.join(list1))
     else:
         print('生成了%s个长度是%s的随机密码' % (n, m))
'''