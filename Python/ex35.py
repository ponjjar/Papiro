a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))


if a < b + c and b < a + c and c < a + b:
    print(f'Os números {a}, {b} e {c} formam um triângulo')
else:
    print(f'Os números {a}, {b} e {c} não formam um triângulo')
