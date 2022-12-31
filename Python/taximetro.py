
def taximetro(tf,tv, distancia):
    conta = tf+(tv*distancia)
    return conta

tf = float(input('insira a taxa fixa: '))
tv = float(input('insira a taxa variavel: '))
distancia = float(input('insira a distancia: '))

print(taximetro(tf, tv, distancia))
