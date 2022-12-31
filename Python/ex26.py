palavra = str(input('Escreva uma palavra: ')).lower() .strip()

conta = palavra.count('a')
pp = palavra.find('a')+1
up = palavra.rfind('a')+1

print(f'conta {conta} \n1 {pp} \nu {up}')