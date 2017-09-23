# coding:utf-8

import urllib
from bs4 import BeautifulSoup
import re
import xlwt
import time


def gethtml(page,n):
	html = urllib.urlopen('http://www.zhipin.com/c101010100/h_101010100/?query=python&page=%s' % page).read()
	soup = BeautifulSoup(html, 'lxml')
	item = soup.find('div', class_='job-list').ul

	for items in item.find_all('li'):
		jobname = items.find('div', class_='job-primary').h3.get_text().encode('utf-8').split()[0]
		wage = items.find('div', class_='job-primary').h3.get_text().encode('utf-8').split()[-1]
		city = items.p.encode('utf-8').split('<em class="vline"></em>')[0].split('<p>')[-1]
		experience = items.p.encode('utf-8').split('<em class="vline"></em>')[1]
		education = items.p.encode('utf-8').split('<em class="vline"></em>')[2].split('</p>')[0]
		companname = items.find('div', class_='info-company').h3.get_text().encode('utf-8')
		companytype = items.find('div', class_='info-company').p.encode('utf-8').split('<em class="vline"></em>')[0].split('<p>')[-1]
		listed = items.find('div', class_='info-company').p.encode('utf-8').split('<em class="vline"></em>')[1]
		scale = items.find('div', class_='info-company').p.encode('utf-8').split('<em class="vline"></em>')[-1].split('</p>')[0]
		hrname = items.find('div', class_='job-tags').p.encode('utf-8').split('<em class="vline">')[0].split('<p>')[-1]
		hrtitle = items.find('div', class_='job-tags').p.encode('utf-8').split('<img')[0].split('</em>')[-1]
		span = items.find('div', class_='job-tags').encode('utf-8')
		reg = r'<span>(.*?)</span>'
		jobcontent = re.findall(reg,span)
		jobcontent = ' / '.join(jobcontent)

		content = {
			'jobname': jobname,
			'wage': wage,
			'city': city,
			'experience': experience,
			'education': education,
			'companytype': companytype,
			'listed': listed,
			'scale': scale,
			'hrname': hrname,
			'hrtitle': hrtitle,
			'jobcontent': jobcontent,
			'companname': companname
		}

		sheet1.write(n, 0, content['jobname'].decode('utf-8'))
		sheet1.write(n, 1, content['jobcontent'].decode('utf-8'))
		sheet1.write(n, 2, content['wage'].decode('utf-8'))
		sheet1.write(n, 3, content['city'].decode('utf-8'))
		sheet1.write(n, 4, content['experience'].decode('utf-8'))
		sheet1.write(n, 5, content['education'].decode('utf-8'))
		sheet1.write(n, 6, content['companname'].decode('utf-8'))
		sheet1.write(n, 7, content['companytype'].decode('utf-8'))
		sheet1.write(n, 8, content['listed'].decode('utf-8'))
		sheet1.write(n, 9, content['scale'].decode('utf-8'))
		sheet1.write(n, 10, content['hrname'].decode('utf-8'))
		sheet1.write(n, 11, content['hrtitle'].decode('utf-8'))
		n += 1
	return n


excelwork = xlwt.Workbook()
sheet1 = excelwork.add_sheet('BOSS', cell_overwrite_ok=True)

sheet1.write(0, 0, '工作岗位'.decode('utf-8'))
sheet1.write(0, 1, '工作内容'.decode('utf-8'))
sheet1.write(0, 2, '工资待遇'.decode('utf-8'))
sheet1.write(0, 3, '城市'.decode('utf-8'))
sheet1.write(0, 4, '工作经验'.decode('utf-8'))
sheet1.write(0, 5, '学历要求'.decode('utf-8'))
sheet1.write(0, 6, '公司名称'.decode('utf-8'))
sheet1.write(0, 7, '公司类型'.decode('utf-8'))
sheet1.write(0, 8, '融资/上市'.decode('utf-8'))
sheet1.write(0, 9, '工司规模'.decode('utf-8'))
sheet1.write(0, 10, '招聘人'.decode('utf-8'))
sheet1.write(0, 11, '招聘人title'.decode('utf-8'))

n = 1
for page in range(1, 31):
	n = gethtml(page=page,n=n)
	print '正在采集第 %s 页' % page
	time.sleep(1)

excelwork.save('BOSS.xls')
print '采集完毕，数据保存在BOSS.xls'