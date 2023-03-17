
print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")    
texto = 'CALCULDORA DE MATRIZ'
print(f'{texto:^37}')
print("\033[31m•\033[32m*\033[33m´\033[34m¨\033[35m`\033[36m*\033[37m•\033[31m.\033[32m¸\033[33m¸\033[34m.\033[35m*\033[36m´\033[37m¨\033[31m`\033[32m*\033[33m•\033[34m.\033[35m¸\033[36m¸\033[37m.•\033[31m*\033[32m´\033[33m¨\033[34m`\033[35m*\033[36m•\033[37m.¸\033[31m¸\033[32m.•\033[33m*\033[34m´\033[35m¨\033[36m`\033[37m•\033[0m")

pares = soma_3c = 0
soma_2l = []
matrix = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        num = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        matrix[l].append(num)
        if num % 2 == 0:
            pares += num
        soma_3c += matrix[l][c] if c == 2 else 0

        #tem que ser uma lista (interável) para poder usar a funcao max()
        soma_2l.append(matrix[l][c]) if l == 1 else 0 

print('\033[36m╔════════════════════════════════════╗\033[0m')
print(f'''               \033[33m{matrix[0]}\033[m 
               \033[34m{matrix[1]}\033[m 
               \033[35m{matrix[2]}\033[m''')
print('\033[36m╚════════════════════════════════════╝\033[0m')
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da 3ª coluna é {soma_3c}.')
print(f'O maior valor da 2º linha é {max(soma_2l)}.')