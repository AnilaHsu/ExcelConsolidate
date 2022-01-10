import xlrd

data = xlrd.open_workbook('A010.xls')
# print('data',data)

table = data.sheets()[0]
# print('table',table)

# 印出每個 sheet 的名字
print(data.sheet_names())

# 印出每個 sheet 每個 column 資料
# for n in range(len(data.sheet_names())):
#     table = data.sheets()[n]

    # for i in range(table.ncols):
    #     print('Page {}: '.format(n), end='')
    #     print(table.col_values(i))