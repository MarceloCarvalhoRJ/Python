my_list = list()
repeated = True

val = int(input('Qtos numeros vc quer inserir na lista?'))

for i in range(val):
    number = float(input('Digite um número: '))
    my_list.append(number)

while repeated:
    repeated = False
    # ordernar a lista de forma decrescente para não gerar erro de 'index out range' por conta da exclusao que eh feita.
    for i in range(len(my_list) - 1, 0, -1): 
        if my_list[i] == my_list[i - 1]:
            del my_list[i]
            repeated = True

print("A lista com os elementos excluídos aqui")
print(my_list)