# pip install xlrd
import xlrd

# 打开excel
wb = xlrd.open_workbook('01_电影数据.xlsx')

# print(wb)
print(f'excel中有{wb.nsheets}个工作薄')
print(f'excel中sheets的名字：{wb.sheet_names()}')
# 选择工作薄
sh1 = wb.sheet_by_index(0)
sh2 = wb.sheet_by_name('电影')
# print(sh1)
# print(sh2)
print(f'sheet里面一共有{sh1.nrows}行 {sh2.ncols}列的数据')

# 获取单元格的值
print(f'第一行第二列的值：{sh1.cell_value(0,1)}')
print(f'第一行第二列的值：{sh1.cell(0,1).value}')
print(f'第一行第二列的值：{sh1.row(0)[1].value}')

# 获取整行或者整列的数据
print(sh1.row_values(0))
print(sh1.col_values(0))

# 遍历所有数据
for r in range(sh1.nrows):
    for c in range(sh1.ncols):
        print(f'第{r}行 第{c}列的数据是 {sh1.cell_value(r,c)}')