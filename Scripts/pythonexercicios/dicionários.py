filmes = {'titulo':'Star Wars','ano': 1977, 'diretor' : 'George Lucas'}

locadora = [{'titulo':'Star Wars','ano': 1977, 'diretor' : 'George Lucas'},
            {'titulo':'Avengers','ano': 2012, 'diretor' : 'Joss Weden'},
            {'titulo':'Matrix','ano': 1999, 'diretor' : 'Machowski'}
            ]

print(filmes['ano']) #1977
print(locadora[0]['diretor']) #George Lucas
print(locadora[2]['titulo']) #Matrix
print(f'O filme é {locadora[1]["titulo"]} do ano de {locadora[1]["ano"]}') #O filme é Avengers do ano de 2012
print(filmes.keys())    #dict_keys(['titulo', 'ano', 'diretor'])
print(filmes.values())  #dict_values(['Star Wars', 1977, 'George Lucas'])
print(filmes.items())   #dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])
for k, v in filmes.items(): #substitui o enumerate() que nao pode ser usado nos dicionários.
    print(f'{k} = {v}')

del locadora[1]['diretor'] #apaga e key e o value. {'titulo': 'Avengers', 'ano': 2012}
print(locadora)

filmes['ano'] = 1978
print(filmes)

filmes['Main Actor'] = 'Mark Hamill' #adiciona nova keys and value to the dictionary.

brasil = [] # criar uma lista para inserir dicionarios.
estado1 = {'UF':'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF':'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil) #[{'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}, {'UF': 'São Paulo', 'Sigla': 'SP'}]
print(brasil[0]) #{'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
print(brasil[1]['UF']) #São Paulo

#joga o for para a mesma linha do input, fechando toda a expressao com [] cria a lista na variavel gols.
partidas = 3
gols = [int(input(f'Quantos gols na partida {c + 1}? ')) for c in range(0, partidas)] 

'''brazil = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brazil.append(estado.copy()) #copia uma lista sem ter relacao
for e in brazil:
    #print(f"{e['uf']} - {e['sigla']}")
    for v in e.values(): #outra maneira de percorrer os valores do dicionário.
        print(v, end = ' ')
    print()'''

#A função len funciona em dicionários; ele retorna o número de pares keys-values:
states = [{'uf': 'Rio', 'sigla': 'RJ'}, {'uf': 'BAhia', 'sigla': 'BA'}, {'uf': 'Acre', 'sigla': 'AC'}]
print(states)
print(len(states))#conta a qtde de dicionarios dentro da lista
print(len(states[0]))#conta os pares keys-values (uf, Rio) + (silga, RJ) = 2
print('.' * 30)
#O operador in também funciona em dicionários; ele dirá se algo aparece no dicionário como uma chave (os valores dos pares não são considerados).
print('uf' in states[0]) #retorna true para as keys
print('RJ' in states[0]) #nao reconhece as values
print('.' * 30)
print('RJ' in states[0].values()) #usar o value() para encontrar valores.

#calcula a media da idade percorrendo a chave idade em cada elemento dentro da variavel cadastro e depois divide pela qtde de pessoas cadastradas.
cadastro = [{'nome': 'Mc', 'sexo': 'm', 'idade': 45}, {'nome': 'Re', 'sexo': 'f', 'idade': 35}]
media_idade = sum(p['idade'] for p in cadastro) / len(cadastro)

#usando o itemgetter(1) da biblioteca operator para extrair o elemento da posicao 1 (value).
jogadas_ordenadas = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
'''outra forma de ordenar pelo valor do dicionario
jogadas_ordenadas = sorted(jogadores.items(), key=lambda x: x[1], reverse=True) #compreensao de dicionario. chama a funcao lambda para informar ao sort() fazer o ordenamento pelo valor quando faço x: x[1] (2º elemento do dicionário que eh o valor)'''