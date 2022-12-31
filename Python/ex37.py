valor = int(input('Digite o número para ser convertido em: '))
sec = int(input('''1: Binário
2: Octal
3: Hexadecimal
'''))

if sec == 1:
    print(bin(valor)[2:])
elif sec == 2:
    print(oct(valor)[2:])
elif sec == 3:
    print(hex(valor)[2:])
else:
    print('Opção invalida!!')