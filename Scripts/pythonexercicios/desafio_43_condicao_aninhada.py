peso = float(input('Informe o seu peso em Kg: '))
altura = float(input('Informe a sua altura em metros: '))
imc = peso / (pow(altura, 2))
peso_ideal = 24.9 * (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está abaixo do peso.')
    print(f'Seu peso ideal seria {18.5 * altura ** 2:.1f}')
elif imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está no peso ideal!')
elif imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está com sobrepeso.')
    print(f'Seu peso ideal seria {peso_ideal:.1f}')
elif imc < 40:
    print(f'Seu IMC é {imc:.1f}. Cuidado, você está Obeso.')
    print(f'Seu peso ideal seria {peso_ideal:.1f}')
else:
    print(f'Seu IMC é {imc:.2f}. Procure um médico. \nVocê possui obesidade mórbida!')
    print(f'Seu peso ideal seria {peso_ideal:.1f}')
