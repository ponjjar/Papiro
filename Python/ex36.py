from time import sleep
vcasa = float(input('Valor da casa: '))
sal = float(input('Valor do salário: '))
anos = int(input('Em quantos anos será a parcela? '))

prest = vcasa / (anos * 12)
meses = anos * 12
por = sal * 0.30

print(f'-=-'*30)
sleep(1)

if prest <= por:
    print(f'''\033[34mPARABÉNS!!\033[m Você pode financiar a casa no valor de R${vcasa:.2f}
Com parcelas de R${prest} 
Em {meses} meses''')
else:
    print(f'\033[31mOPS!!\033[m Infelizmente não podemos aprovar, pois a prestação excede os 30% do seu salário')
