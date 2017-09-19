# coding:utf-8
import urllib
import re



def getList(page):
    url = 'http://www.xiaohuar.com/list-1-%s.html' %page
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<a href="(.*?)"  target="_blank"><img width="210"  alt="(.*?)"'
    reg = re.compile(reg)
    picurl = re.findall(reg,html)
    return picurl

def images(picurl):
    if len(picurl) > 20: #检查无效地址
        html = urllib.urlopen(picurl).read().decode('gbk', 'ignore').encode('utf-8', 'ignore')
        reg = r'<a target="_blank" class="imglink" href="(.*?)"><img alt='
        reg = re.compile(reg)
        imglink = re.findall(reg,html)
        if str(imglink) == '[]':
            pass
        else:
            imglink = imglink[0]
            html = urllib.urlopen(imglink).read()
            reg = r'class="inner"><a href="(.*?)" class="">'
            reg = re.compile(reg)
            imgurl = re.findall(reg,html)
        return imglink
    else:
        return None



for i in range(0,44):
    a = i + 1
    print '###################'
    print '正在爬取第 %s 页' % a
    print '###################'
    for picurl,title in getList(page=i): #获取相册地址和相册名
        num = 1
        if images(picurl) != None :
            for imgurl in images(picurl=picurl): #获取相册集
                if imgurl != []:
                    imgurls = 'http://www.xiaohuar.com%s' %imgurl #照片完整地址
                    imgdir = '/Users/tao/Pictures/校花/%s' % title
                    urllib.urlretrieve(imgurls, imgdir + '%s.jpg' % num)
                    print '%s 保存成功' % title
                    num += 1
                else:
                    print '未获取到 %s 图片地址' %title
        else:
            print '%s 地址无效 - 跳过' %picurl




