nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Sua média é {media:.2f} e vc foi APROVADO!')
elif 7 > media >= 5: # outra forma de testar valores entre numeros.
    print(f'Sua média é {media:.2f} e você está de recuperação.')
else:
    print(f'Sua média é {media:.2f} e infelizmente você foi reprovado!')
