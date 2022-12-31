from datetime import date

def anos(ano):
    anoatual = date.today().year
    
    idade = anoatual - ano
    prazo = 18 - idade
    anoma = anoatual + prazo
    anome = anoatual + prazo

    if ano > anoatual:
        print(f'Você é do futuro ')
    elif ano < 1930:
        print(f'Você é um dinossauro')
    elif idade > 19:
        print(f'''Já passou {prazo * -1} anos do tempo de se alistar
Você tinha q se alistar em {anome}''')
    elif idade == 19:
        print(f'''Já passou 1 ano do tempo de se alistar
Você tinha q se alistar em {anome}''')
    elif idade < 17:
        print(f'''Você tem que se alistar daqui {prazo} anos
Vai ter que se alistar em {anoma}''')
    elif idade == 17:
        print(f'''Você tem que se alistar daqui 1 ano
Vai ter que se alistar em {anoma}''')
    else:
        print(f'Você tem que alistar esse ano')

ano = int(input('Digite o ano de nascimento: '))
anos(ano)