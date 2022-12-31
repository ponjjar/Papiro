def triangulo(ld1, ld2, ld3):
    if ld1 > (ld2 + ld3) or ld2 > (ld1 + ld3) or ld3 > (ld1 + ld2):
        print(f'As medidas {ld1}, {ld2} e {ld3} não formam um triângulo')
    elif ld1 == ld2 == ld3:
        print(f'As medidas {ld1}, {ld2} e {ld3} formam um triângulo quilátero')
    elif ld1 == ld2 or ld1 == ld3 or ld2 == ld3:
        print(f'As medidas {ld1}, {ld2} e {ld3} formam um trângulo isósceles')
    elif ld1 != ld2 or ld1 != ld3 or ld2 != ld3:
        print(f'As medidas {ld1}, {ld2} e {ld3} formam um trângulo escaleno')


ld1 = float(input('Digite o 1º lado do triângulo: '))
ld2 = float(input('Digite o 2º lado do triângulo: '))
ld3 = float(input('Digite o 3º lado do triângulo: '))

triangulo(ld1, ld2, ld3)