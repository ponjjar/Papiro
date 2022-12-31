sal = float(input('Digite o salário do funcionário: '))

if sal > 1250.00:
    au = sal * 0.10 + sal
else:
    au = sal * 0.15 + sal
    
print(f'O novo salário será de R${au}')