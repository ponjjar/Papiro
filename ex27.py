n = str(input('Digite seu nome: ')).strip()

nome = n.split()
pn = nome[0]
un = nome[len(nome) -1]

print(f'{n} \n{pn} \n{un}')
