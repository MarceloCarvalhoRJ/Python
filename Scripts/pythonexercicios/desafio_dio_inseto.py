C = int(input()) 
for i in range (C):
    num = int(input())
    print("Mais de 8000!" if num > 8000 else "Inseto!")
    # print("Mais de 8000!" if int(input()) > 8000 else "Inseto!")


'''
import sys

C = int(sys.stdin.readline())
for i in range (C): 
    num = int(input())
    if 100 <= num <= 8000:
      print('Inseto!')
    elif 8000 <= num <= 100000:
      print('Mais de 8000!')
'''      