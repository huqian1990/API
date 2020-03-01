import re
from urllib import request
import urllib

#获取整个网页代码
def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

#正则匹配——获取图片
# def getImg(html):
#     reg=r'src="(.*?\.jpg)"width'
#     imgre=re.compile(reg)
#     imglist=re.findall(imgre,html.decode("utf-8"))
#     return imglist

#
def getImg1(html):
    reg=r'src="(.*?\.jpg)"width'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html.decode("utf-8"))
    x=0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg'%x)
        x=x+1

codes=getHtml("http://tieba.baidu.com/p/2460150866")
# print(codes)
print(getImg1(codes))