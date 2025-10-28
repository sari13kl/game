import math
a = float(input('Comprimento do cateto oposto: \n'))
b = float(input('Comprimento do cateto adjacente: \n'))
c = math.hypot(a, b)
print(f'O valor da sua hipotenusa é {c}')