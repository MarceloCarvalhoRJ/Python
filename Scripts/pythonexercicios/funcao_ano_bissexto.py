
def ano_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


list_years = [40, 1540, 1800, 2000, 2023]
for year in list_years:
    if ano_bissexto(year) == True:
        print(f'O ano {year} é Bissexto!')
    else: 
        print(f'O ano {year} NÃO É bissexto.')
