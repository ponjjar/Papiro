from random import randint
from time import sleep

print('-=-'*20)
print('vou pensar em um úmero de 0 até 5. Tente adivinhar...')
print('-=-'*20)
numero = int(input('Em que número eu pensei? '))

numa = randint(0, 5)

print(f'PROCESSANDO...')
sleep(3)

if numero == numa:
    print('PARABÉNS. Você me venceu!')
else:
    print(f'GANHEI!. Eu pensei no número {numa} e não no {numero}')

