hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.
print('Lista: ', hat_list)

hat_list[2] = int(input(f'Substitua o numero {hat_list[2]} por outro: '))

print('Vamos deletar o numero', hat_list[4])

del hat_list[-1]

print ('Aqui está a lista atualizada: ', hat_list) 
print('.' * 40)

numbers = [111, 7, 2, 1]

print(len(numbers))

print(numbers)

numbers.append (4)

print(len(numbers))

print(numbers)

numbers.insert (0, 222)
numbers.insert(1, 333)
print('.' * 40)

my_list = [] # Criando uma lista vazia.

for i in range(5):
   my_list.append (i + 1)

print (my_list)


my_list = []  # Criando uma lista vazia.
 
for i in range(5):
    my_list.insert(0, i + 1) #usando o insert para obter uma lista na ordem inversa
 
print(my_list)
print('.' * 40)

my_list = [10, 1, 8, 3, 5]

total = sum(my_list)

#for i in range(len(my_list)):

  #total += my_list[i]

print(total)

my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)
print('.' * 40)

print(my_list)
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)
print('.' * 40)

my_lyst = [10, 1, 8, 3, 5]

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)
print('.' * 40)

beatles = []

print("Etapa 1:", beatles)

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George')

print("Etapa 2:", beatles)

for i in range(2):
    new_member = input('Insira novo integrante da banda: ')
    beatles.append(new_member)
    
print("Etapa 3:", beatles)

del beatles[3:]

print("Etapa 4:", beatles)

beatles.insert(0, 'Ringo Starr')

print("Etapa 5:", beatles)
