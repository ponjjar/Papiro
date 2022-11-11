viagem = float(input('Quantos km você vai viajar? '))

vf = viagem * 0.50 if viagem <= 200 else viagem * 0.45

print(f'Sua viagem ficará R${vf}.')

# if viagem <= 200:
#     vf = viagem * 0.50
# else:
#     vf = viagem * 0.45

# print(f'Sua viagem ficará R${vf}.')
    