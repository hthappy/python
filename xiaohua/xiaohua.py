# coding:utf-8
import urllib
import re
import os



def getList(page):
    url = 'http://www.xiaohuar.com/list-1-%s.html' %page
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<a href="(.*?)"  target="_blank"><img width="210"  alt="(.*?)"'
    reg = re.compile(reg)
    picurl = re.findall(reg,html)
    return picurl

def images(picurl):
    html = urllib.urlopen(picurl).read().decode('gbk', 'ignore').encode('utf-8', 'ignore')
    reg = r'<a target="_blank" class="imglink" href="(.*?)"><img alt='
    regs = r'<img src=\\\'(.*?)\\\' alt=\\\''
    if re.findall(r'imglink',html) != []:  #判断是否正常页面
        reg = re.compile(reg)
        imglink = re.findall(reg, html)
        html = urllib.urlopen(imglink[0]).read().decode('gbk', 'ignore').encode('utf-8', 'ignore')
        reg = r'class="inner"><a href="(.*?)" class="">'
        reg = re.compile(reg)
        imgurl = re.findall(reg, html)
        return imgurl
    else:
        regs = re.compile(regs)
        imgurl = re.findall(regs,html)
        return imgurl




for i in range(0,44):
    a = i + 1
    print '###################'
    print '正在爬取第 %s 页' % a
    print '###################'
    for picurl,title in getList(page=i): #获取相册地址和相册名
        num = 1
        for imgurl in images(picurl=picurl): #获取相册集
            imgurls = 'http://www.xiaohuar.com%s' %imgurl #照片完整地址
            imgdir = '/Users/tao/Pictures/校花/%s/' % title #保存目录
            if os.path.isdir(imgdir):
                urllib.urlretrieve(imgurls, imgdir + '%s.jpg' % num)
                print '%s 保存成功' % title
                num += 1
            else:
                os.makedirs(imgdir)
                urllib.urlretrieve(imgurls, imgdir + '%s.jpg' % num)
                print '%s 保存成功' % title
                num += 1





