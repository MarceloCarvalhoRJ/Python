def introduction(first_name, last_name='Smith'):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse")
introduction("Clark")
print()

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, c=1, b=2)
print()

def introduction_02(first_name="John", last_name="Smith"):
    print("Olá meu nome é", first_name, last_name)

introduction_02()
print()

def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes:
        return
    print("Feliz Ano Novo!")

happy_new_year()
print()

def boring_function():
    return 123
 
x = boring_function()
 
print("A boring_function retornou seu resultado. Isso é:", x)
print()

def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
 

print(strange_list_fun(5))


