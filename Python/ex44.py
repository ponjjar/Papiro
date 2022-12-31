def desdv(produto):
    desconto = produto - (produto * 0.10)
    print(f'Valor da compra com 10% desconto é de R${desconto}')

def descv(produto):
    desconto = produto - (produto * 0.05)
    print(f'Valor da compra com 5% desconto é de R${desconto}')

def parc2(produto):
    parcela = produto / 2
    print(f'2x: R${parcela}')

def parc(produto):
    parcela = produto + (produto * 0.20)
    for i in range(3,13):
        par = parcela / i
        print(f'{i}x: R${par:.02f}')

def sep():
    print(f'-=-'*20)

sep()
produto = float(input('Valor do produto:'))
sep()
pagamento = int(input(f'''Formas de pagamento:
1: À vista no dinheiro com 10% de desconto.
2: À vista no cartão com 5% de desconto.
3: 2x no cartão s/j.
4: Até 12 vezes com 20% de jusros sob o valor total.
'''))
sep()
if pagamento == 1:
    desdv(produto)
elif pagamento == 2:
    descv(produto)
elif pagamento == 3:
    parc2(produto)
elif pagamento == 4:
    parc(produto)
