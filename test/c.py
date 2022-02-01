import xlsxwriter as xw

create_xlsx = xw.Workbook(r"D:\GithubRepositories\GoldCalculation\P.xlsx")
create_xlsx.add_worksheet()

create_xlsx.close()