# aList = [123, 'Google','qqqqqqqqqqqqq', 'Rob',23,"ww",'Taobao1122',"ww",1]  ##字符串包含数字和字符
#
# #声明2个空列表用作存放不同类型的数据
# aint=[]
# bstr=[]
#
#
# #int和str分别存放到列表中
# def find():
#     for i in aList:
#         if isinstance(i, int):
#             aint.append(i)
#         else:
#             bstr.append(i)
#     return aint,bstr
#
# #数字大的基本就是长度长的，所以这里只要排序就好
# def find_num():
#     a=find()
#     aint=a[0]
#     aint.sort()
#     anum=((aint[-1]))
#     print("列表中最长的数字是：",(anum))
#
# #
# def find_str():
#     a = find()
#     bstr = a[1]
#
#     for i in range(len(bstr)-1):
#         min = i
#         for j in range(i+1,len(bstr)):
#             if len(bstr[i]) >= len(bstr[j]):
#                 min = j
#                 bstr[i], bstr[min] = bstr[min], bstr[i]
#     print("列表中最长的字符是：", (bstr[-1]))
# if __name__=="__main__":
#     t=find()
#     print("数字列表为{}：".format(t[0]),"字母列表为{}：".format(t[1]))
#     find_num()
#     find_str()



#
# lista=[1,2,3,4,5,['2a','ff',['你好',[222,33,44]],'gass']]
# def func(L):
#         for i in L:
#                 if (isinstance(i, list)):
#                         func(i)
#                 else:
#                         print(i)
# if __name__=="__main__":
#         func(lista)



lista=[1,2,3,4,5,['2a','ff',['你好',[222,33,44]],'gass']]
new=str(lista).split("[")
for i in new:
        if i ==","or i=='':
                new.remove(i)
print(new)














