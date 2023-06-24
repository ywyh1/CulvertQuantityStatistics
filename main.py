import openpyxl as xl

# 打开涵洞一览表，获取要统计工程量的涵洞信息
wb2 = xl.load_workbook('./涵洞一览表.xlsx')
ws = wb2["涵洞一览表"]

#工程名称
projectName = ws['A3']

#获取逐行涵洞信息
for row in ws.rows:
    if row[1].row < 6:
        continue
    if row[2].value != None:
        print(row)
        print(row)



