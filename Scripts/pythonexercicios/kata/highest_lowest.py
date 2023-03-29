
def high_and_low(numbers):
    num = [int(c) for c in numbers.split()]
    return f'{max(num)} {min(num)}'

print(high_and_low('2 -51 7 19 1 -42'))
