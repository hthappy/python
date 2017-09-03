# coding:utf-8
import urllib
import re
import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'test',
    charset = 'utf8'
) #连接数据库

cur = conn.cursor()

def getList(page):
    html = urllib.urlopen('http://www.dytt8.net/html/gndy/dyzz/list_23_%s.html' %page)
    text = html.read()
    text = text.decode('GBK','ignore').encode('utf-8','ignore')  #转码
    reg = r'<a href="(.+?)" class="ulink">(.+?)</a>' #正则匹配
    return re.findall(reg,text)

def getContent(url):
    html = urllib.urlopen('http://www.dytt8.net%s' %url).read()
    content_text = html.decode('gbk','ignore').encode('utf-8','ignore')
    reg = r'<div class="co_content8">(.*?)<p><strong><font color="#ff0000" size="4">'
    reg = re.compile(reg,re.S)
    text = re.findall(reg,content_text)

    if text:
        text = text[0]
    reg = r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">'
    link = re.findall(reg,content_text)
    if link:
        link = link[0]
    return text,link

for i in range(1,164):
    for url,title in getList(page = i):
        print '正在爬取第 %s 页的 %s' %(i,title)
        content,link = getContent(url)
        if content:
            print '正在保存第 %s 页的 %s' %(i,title)
            cur.execute("insert into movie(id,title,content,link) values (NULL ,'%s' ,'%s' ,'%s')" %(title,content.replace("'",r"\'"),link)) #执行SQL语句
            conn.commit() 