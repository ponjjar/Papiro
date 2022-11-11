from datetime import date

def categorias(ano):
    idade = date.today().year - ano

    if idade <= 9:
        print(f'Sua idade é {idade} e você é da categoria MIRIM')
    elif idade <= 14: 
        print(f'Sua idade é {idade} e você é da categoria INFANTIL')
    elif idade <= 19: 
        print(f'Sua idade é {idade} e você é da categoria SÊNIOR')
    else: 
        print(f'Sua idade é {idade} e você é da categoria MASTER')

ano = int(input('Digite o ano do atleta: '))
categorias(ano)