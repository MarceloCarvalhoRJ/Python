my_list = list()

val = int(input('Qtos numeros vc quer inserir na lista?'))

for i in range(val):
    number = float(input('Digite um número: '))
    my_list.append(number)

my_list_no_repeat = list(set(my_list))

print("A lista com os elementos excluídos aqui")
print(my_list_no_repeat)