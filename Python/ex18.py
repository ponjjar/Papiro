from math import sin, cos, tan, radians
an = float(input('Digite o ângulo: '))

sin = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))

print(f'O valor do seno é {sin:.2f}. \nO valor do cosseno é {cos:.2f}. \nO valor da tangente é {tan:.2f}.')