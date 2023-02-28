month = int(input('What month were you born? [1 to 12]? '))
if month < 1 or month > 12:
    print('Valor inválido! O nr. deve estar entre 1 e 12.')
else:
    months_dict = {
    1: 'january', 
    2: 'february', 
    3: 'march', 
    4: 'april', 
    5: 'may', 
    6: 'june', 
    7: 'july', 
    8: 'august', 
    9: 'september', 
    10: 'october', 
    11: 'november', 
    12: 'december'
    }
    print('The month is {}'.format(months_dict[month].capitalize()))
