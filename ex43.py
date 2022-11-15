def imc(altura, peso):
    result = peso / (altura ** 2)
    if result < 18.5:
        print(f'O seu imc é {result:.2f} e você está abaixo do peso')
    elif result <= 25:
        print(f'O seu imc é {result:.2f} e você está no peso ideal')
    elif result <= 30:
        print(f'O seu imc é {result:.2f} e você está sobrepeso')
    elif result <= 40:
        print(f'O seu imc é {result:.2f} e você na obesidade')
    else:
        print(f'O seu imc é {result:.2f} e você está na obesidade mórbida')

altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc(altura, peso)
