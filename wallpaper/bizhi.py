# coding:utf-8

#彼岸桌面，采集所有壁纸，地址：http://www.netbian.com/

import urllib
import re
import os


def getHtml(page):
    # 匹配图片列表地址
    url = 'http://www.netbian.com/index_%s.htm' % page
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<li><a href="(.*?)" title="(.*?)" target='
    imglist = re.findall(reg, html)
    return imglist


def getimage(url):
    imageurl = 'http://www.netbian.com%s' % url
    html = urllib.urlopen(imageurl).read().decode('gbk').encode('utf-8')  # 获取图册html
    reg = '<span class="actionb">.*? <a href="(.*?)" target="_blank"'
    imageurl = re.findall(reg, html)[0]  # 匹配壁纸下载页
    imageurl = 'http://www.netbian.com%s' % imageurl  # 壁纸下载页完整地址
    html = urllib.urlopen(imageurl).read()
    reg = r'<img src="(.*?)" title='
    image = re.findall(reg, html)
    return image


for i in range(2, 1134):
    for imglist, title in getHtml(page=i):
        num = 1
        for imageurl in getimage(url=imglist):
            savepath = '/Users/tao/Pictures/wallpaper/%s' % title
            urllib.urlretrieve(imageurl, savepath + '%s.jpg' % num)
            print '正在采集第 %s 页' %i
            print '%s 已保存到本地！' %title
            num += 1

print '采集完毕，退出！'