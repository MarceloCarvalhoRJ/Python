
def is_prime(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True
        
for i in range(1, 101):
    if is_prime(i):
        print(i, end = ' ')
        


