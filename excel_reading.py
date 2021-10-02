import openpyxl

wb = openpyxl.load_workbook('store.xlsx')

print(wb.sheetnames)

for sheet in wb:
    print(sheet.title)

sheet = wb['Products']
sheet = wb.active

b2_cell = sheet['B2']
c2_cell = sheet['c2']

print(b2_cell.value, c2_cell.value)

sheet = wb.active
sheet['d2'] = 400
new_product = (11, 'Tablet', 12, 600)
wb.save('store.xlsx')



