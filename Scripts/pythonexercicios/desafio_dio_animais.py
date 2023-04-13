a = input() 
b = input()     
c = input() 

animals = {'vertebrado': 
          {'ave':{'carnivoro': 'aguia', 'onivoro':'pomba'},
          'mamifero': {'onivoro':'homem', 'herbivoro':'vaca'}
          },'invertebrado':
          {'inseto': {'hematofago':'pulga', 'herbivoro':'lagarta'},
           'anelideo': {'hematofago':'sanguessuga', 'onivoro':'minhoca'}}
          }
print(animals[a][b][c])

{'vertebrado': {'ave':{'carnivoro': 'aguia', 'onivoro':'pomba'},'mamifero': {'onivoro':'homem', 'herbivoro':'vaca'}},'invertebrado':
{'inseto': {'hematofago':'pulga', 'herbivoro':'lagarta'},'anelideo': {'hematofago':'sanguessuga', 'onivoro':'minhoca'}}}

'''
if a == 'vertebrado': 
  if b == 'ave':
     print('aguia' if c == 'carnivoro' else 'pomba')
  elif b == 'mamifero':
     print('homem' if c == 'onivoro' else 'vaca')
  
elif a == 'invertebrado':
  if b == 'inseto':
    print('pulga' if c == 'hematofago' else 'lagarta')
  elif b == 'anelideo':
    print('sanguessuga' if c == 'hematofago' else 'minhoca')
'''
