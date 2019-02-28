import xlrd
import csv
from datetime import date

def excel_to_csv(inputPath, outputPath, delimiter = ","):
    wb = xlrd.open_workbook(inputPath)
    sheetNames = wb.sheet_names()
    
    for idx, val in enumerate(sheetNames):
        sh = wb.sheet_by_name(sheetNames[idx])
        
        with open(outputPath + str(val) + '-' + str(date.today().isoformat()) + '.csv', 'w', newline = "", encoding = 'utf-8') as csvOut:
            wr = csv.writer(csvOut, delimiter = delimiter, quoting = csv.QUOTE_ALL)
            
            for rownum in range(sh.nrows):
                with_newline = sh.row_values(rownum)
                without_newline = [str(s).replace("\n", " ") for s in with_newline]
                wr.writerow(without_newline)
                
            csvOut.close()

excel_to_csv(r"< Path >\< File Name > .xlsx", r'< Path >', "|")
