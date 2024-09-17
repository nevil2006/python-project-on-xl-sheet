import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
print(wb.sheetnames) 
sheet = wb['Sheet1']

for row in range(1, sheet.max_row + 1):
    cell = sheet.cell(row, 3)

    if isinstance(cell.value, (int, float)):
        corrected_price = cell.value * 0.9  
    else:
        corrected_price = cell.value  

    corrected_price_cell = sheet.cell(row, 4)
    corrected_price_cell.value = corrected_price

wb.save('transactions2.xlsx')
