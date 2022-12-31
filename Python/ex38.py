def maior(num1, num2):
    if num1 > num2:
        print(f'O 1º número {num1} é maior.')
    elif num2 > num1:
        print(f'O 2º número {num2} é maior.')
    else:
        print(f'Os números {num1} e {num2} são iguais.')


num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
maior(num1, num2)