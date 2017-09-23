# coding:utf-8
#python3

import requests
import xlwt

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
# 来路页面
	'Cookie': 'user_trace_token=20170518214834-bbd34ec9d493415d9e2d2e13bf6e407d; LGUID=20170518214834-afcdec43-3bd0-11e7-84e0-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEEAAJA4432FC2A3FCC1569A9D525DA0E4346F4; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; _gid=GA1.2.1925284753.1505652316; _gat=1; _ga=GA1.2.1399679985.1495115314; LGSID=20170917204516-0e17f39e-9ba6-11e7-9196-5254005c3644; LGRID=20170917211510-3b5d0600-9baa-11e7-9196-5254005c3644; SEARCH_ID=d307a2ccc08e43fcb1497be6925c6748'
}


def getJoblist(page):
	formdata = {
		'first': 'false',
		'pn': page,
		'kd': 'python'
	}
	res = requests.post(
		'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0',
		data=formdata, headers=headers)  # 发起一个POST请求
	result = res.json()
	jobs = result['content']['positionResult']['result']
	return jobs


excelTable = xlwt.Workbook()  # 创建excel对象
sheet1 = excelTable.add_sheet('lagou', cell_overwrite_ok=True)

sheet1.write(0, 0, '公司名称')
sheet1.write(0, 1, '工作地点')
sheet1.write(0, 2, '工作岗位')
sheet1.write(0, 3, '月薪待遇')
sheet1.write(0, 4, '工作经验')
sheet1.write(0, 5, '学历要求')
sheet1.write(0, 6, '公司规模')
sheet1.write(0, 7, '行业领域')
sheet1.write(0, 8, '福利优势')

n = 1

for page in range(1, 31):
	for job in getJoblist(page=page):
		sheet1.write(n, 0, job['companyShortName'])
		sheet1.write(n, 1, job['city'])
		sheet1.write(n, 2, job['positionName'])
		sheet1.write(n, 3, job['salary'])
		sheet1.write(n, 4, job['workYear'])
		sheet1.write(n, 5, job['education'])
		sheet1.write(n, 6, job['companySize'])
		sheet1.write(n, 7, job['industryField'])
		sheet1.write(n, 8, job['positionAdvantage'])
		n += 1
	print('正在采集第 %s 页' %page)

excelTable.save('lagou.xls')
print('采集完毕，保存到lagou.xls')
