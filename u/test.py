import xlrd
import numpy as np

workbook = xlrd.open_workbook(r'C:\Users\Theo\Desktop\test.xlsx')
worksheet = workbook.sheet_by_index(0)
tabl = "["
for i in range(worksheet.nrows):
    tabl = tabl + "["

    for j in range(worksheet.ncols):
        v=worksheet.cell_value(i,j)
        v= v.replace("i","j")
        tabl = tabl + v + ","
    tabl = tabl[:-1]+ "],"
tabl = tabl[:-1] +"]"

print(tabl)

        