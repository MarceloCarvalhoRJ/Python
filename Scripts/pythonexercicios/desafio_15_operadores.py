totdia = int(input('Quantos dias alugados? '))
totkm = int(input('Quantos km rodados? '))
DIA = 60
KM = 0.15
total = (totdia * DIA)  + (totkm * KM)
print(f'O total a pagar é de R$ {total:.2f}')