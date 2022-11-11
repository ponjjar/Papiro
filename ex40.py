def media(nt1, nt2):
    md = (nt1 + nt2) / 2
    print(md)

    if md < 5:
        print(f'Sua média é {md:.2f} e você foi reprovado')
    elif md < 7:
        print(f'Sua média é {md:.2f} e você esta de recuperação')
    else:
        print(f'Parabéns sua média é {md:.2f} e você foi aprovado')

nt1 = float(input('Digite a 1ª nota do aluno: '))
nt2 = float(input('Digite a 2ª nota do aluno: '))

media(nt1, nt2)