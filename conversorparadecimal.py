def conversor(decimal, base):
    final = []
    numeroDividido = decimal
    while numeroDividido > 0:
        final.append( numeroDividido -( base  * (numeroDividido // base)))
        numeroDividido  //= base
    return(final[::-1])
decimal = int(input('Digite o decimal: '))
base = int(input('Digite a base: '))
print(conversor(decimal, base))