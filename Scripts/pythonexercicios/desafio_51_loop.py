print('=' * 30)
print(f"{'10 TERMOS DE UMA PA':^30}") # centraliza o texto no espaço de 30 caracteres usando a f-string
print('=' * 30)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = primeiro_termo
print(primeiro_termo, end = ' → ')
for i in range(1, 10):
    pa += razao
    print(pa, end = ' → ')
print('Acabou!')