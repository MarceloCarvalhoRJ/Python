
cadastro = list()

while True:
    pessoa = dict() #a variavel tem que estar dentro do Loop para poder armazenar todas as pessoas.
    pessoa['nome'] = input('Nome: ').title()
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0] #pega somente a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!, por favor digite apenas M ou F.')  
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa)
    while True:
        opcao = input('Deseja continunar [S/N]? ').upper()[0] #pega somente a primeira letra
        if opcao in 'SN':
            break
        print('ERRO! Digite somente S ou N.')
    if opcao in 'N':
        break
#calcula a media da idade percorrendo a chave idade em cada elemento dentro da variavel cadastro e depois divide pela qtde de pessoas cadastradas.
media_idade = sum(p['idade'] for p in cadastro) / len(cadastro)
mulheres_cad = [m['nome'] for m in cadastro if m['sexo'] in 'Ff']
mulheres = ','.join(mulheres_cad).replace(',', ' - ')  
print(cadastro)
print('-=' * 30)
print(f'A) O grupo tem {len(cadastro)} pessoas.')
print(f'B) A média de idade é de {media_idade:.2f} anos')
print(f'C) As mulheres cadastradas foram: {mulheres}.')
print(f'D) Lista das pessoas que estão acima da média:')        
for p in cadastro:
    if p['idade'] > media_idade:
        for key, value in p.items():
            print(f'{key} = {value};', end = ' ')
        print()
print('««« ENCERRADO »»»')            

        
    
