teste = list()
galera = list()
teste.append('Marcelo')
teste.append(50)
galera.append(teste[:]) # copia a lista teste mas sem fazer a vinculacao
teste[0] = 'Maria'
teste[1] = 21
galera.append(teste[:])

print(teste)     # ['Maria', 21]
print(galera)    # [['Marcelo', 50], ['Maria', 21]]

for p in galera:
    print(p[0])  # Marcelo 
                 # Maria
for p in galera:
    print(p[1])  # 50
                 # 21 
for p in galera:
    print (f'{p[0]} tem {p[1]} anos de idade.')  # Marcelo tem 50 de idade.
                                                 # Maria tem 21 de idade.
print('.' * 40, '\n')

dado = []
galera = list()

for i in range(0, 3):
    dado.append(input('Qual é o seu nome? '))
    dado.append(int(input('Idade? ')))
    galera.append(dado[:])
    dado.clear()

print('.' * 40)
print(galera)
for p in galera:
    print (f'{p[0]} tem {p[1]} anos de idade.')
print('.' * 40)
for p in galera:    
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade')


