nome = str(input('Digite seu nome completo: ')).strip()

M = nome.upper()
m = nome.lower()
lt = len(nome) - nome.count(' ')
pn = nome.find(' ')

print(f'''Nome em maiúsculo: {M}. \nNome em minúsculo: {m}. 
Quanridade de letras sem o espaço: {lt}. \nQuantidade de letras do 1º nome: {pn}.''')