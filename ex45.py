from random import randint
from time import sleep

def pc(esc):
    opcoes = ['Pedra', 'Papel','Tesoura']
    ale = randint(1, 3)

    if ale == esc:
        print(f'Deu empate: usuário {opcoes[esc -1]}: pc {opcoes[ale -1]}')
    elif ale == 2 and esc == 1 or ale == 3 and esc == 2 or ale == 1 and esc == 3:
        print(f'O Pc ganhou: usuário {opcoes[esc -1]}: pc {opcoes[ale - 1]}')
    elif ale == 1 and esc == 2 or ale == 2 and esc == 3 or ale == 3 and esc == 1:
        print(f'Você ganhou: usuário {opcoes[esc -1]}: pc {opcoes[ale - 1]}')


esc = 0
while esc < 1 or esc > 3:
    esc = int(input('''Digite um número:
1 = Pedra
2 = Papel
3 = Tesoura
'''))
    if esc < 1 or esc > 3:
        print("opção invalida, escolha outra")
sleep(0.5)
print(f'JO')
sleep(0.5)
print('KEN')
sleep(0.4)
print('POO')

pc(esc)
