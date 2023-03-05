
names = ('table', 'chair', 'sofa', 'fridge', 'oven', 'microwave', 'stove', 'cupboard', 'pantry', 'sink', 'dishwasher', 'washing machine', 'dryer')
for name in names:
    print(f'\nNa palavra \033[33m{name.upper()}\033[0m possui as vogais:', end = ' ')
    for letra in name:
        if letra.lower() in 'aeiou':
            print(f'\033[36m{letra.upper()}\033[0m', end = ' ')
