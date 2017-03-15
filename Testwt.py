#coding:utf-8
import xlwt
from datetime import datetime

style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'SimSun'              #指定‘宋体’
style.font = font

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook(encoding = 'utf-8')      #注意这里的写法格式，很重要的一个点
ws = wb.add_sheet('汇总')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))
ws.write(3,0,"Monday")
ws.write(4,0,"你好")
ws.write(5,0,1234)
wb.save('/Users/vilogy/testwt.xls')
