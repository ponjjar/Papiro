# from random import choice

# lista = []
# for n in range(1,5):
#     nome = input(f'{n}° Aluno: ')
#     lista.append(nome)

# a = []
# for s in range(1,5):
#     sorteio = choice(lista)
#     a.append(sorteio)
#     lista.remove(sorteio)
# print(a)

from random import shuffle

lista = []
for n in range(1,5):
    nome = input(f'{n}° Aluno: ')
    lista.append(nome)
shuffle(lista)
print(lista)
