from re import A


l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l * a 
p = ar / 2

print(f'Sua parede tem a dimensão de {l} x {a} e a sua área é de {ar} m².')
print(f'Para pintar essa parede, você precisará de {p} l de tinta')
