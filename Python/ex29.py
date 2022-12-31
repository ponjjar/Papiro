vel = float(input('Qual a velocidade do carro:'))

if vel > 80:
    multa = vel - 80
    pagar = multa * 7
    print(f'Você foi multado e você pagará R${pagar} de multa')

print('Tenha um bom dia e dirija com segurança')
