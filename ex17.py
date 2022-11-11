from math import hypot

ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
h1 = hypot(ca, co)

print(f'{h1:.2f}')
