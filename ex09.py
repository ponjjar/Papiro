n = int(input('Digite um número para ver sua tabuada: '))

print(f'-'* 12)

for i in range(0, 11):
    t = i * n
    print(f'{i:0>2} x {n} = {t:0>2}')

print(f'-'* 12)
