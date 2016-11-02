# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.11
    @FileName：   xlsx_2.py -v1.0
    @Author:      cnshhi
    @CreateTime:  2016/10/31 10:45
    @Description:
    多个工作表
    并写入简单数据
"""

import xlsxwriter

workbook = xlsxwriter.Workbook('slsx.xlsx')
worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet('Foglio2')
worksheet3 = workbook.add_worksheet('Data')
worksheet4 = workbook.add_worksheet(u'工作表')

worksheet1.set_column('A:A',20)
bold = workbook.add_format({'bold':True})

worksheet1.write('A1','hello')
worksheet1.write('A2','word',bold)
worksheet1.write('B2',u'中文测试',bold)

worksheet1.write(2,0,32)
worksheet1.write(3,0,35.5)
worksheet1.write(4,0,'=SUM(A3:A4)')


workbook.close()