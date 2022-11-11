from random import choice

lista = []
for a in range(1,5):
    nome = input(f'{a}° Aluno: ')
    lista.append(nome)
    sorteio = choice(lista)

print(f'O aluno sorteado foi: {sorteio}')
