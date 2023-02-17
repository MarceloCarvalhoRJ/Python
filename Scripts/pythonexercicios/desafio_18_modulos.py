from math import radians, sin, cos, tan
a = float(input('Informe o angulo º '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print(f'O angulo {a:.0f}º possui:\nSENO de {seno:.2f} \nCOSSENO de {cosseno:.2f} \nTANGENTE de {tangente:.2f}')
