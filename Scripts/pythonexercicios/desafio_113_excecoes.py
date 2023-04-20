def leiaint():
    while True:
        try:
            num = int(input('Digite um numero inteiro: '))
            return num
        
        except ValueError:
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[31mErro! O usuário preferiu não digitar esse número.\033[m')
            return 0


def leiareal():
        while True:
            try:
                num = float(input('Digite um numero real: '))
                return num
            
            except ValueError:
                print('\033[31mErro! Por favor, digite um número real válido.\033[m')

            except KeyboardInterrupt:
                print('\n\033[31mErro! O usuário preferiu não digitar esse número.\033[m')
                return 0      


inteiro=leiaint()
real = leiareal()
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real} ')

