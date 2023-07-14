#Calculadora

valor = int(input("Digite o valor que você deseja calcular: "))

print("O valor digitado foi: ", valor)
# +, -, *, /
operacao = input("Digite o operador que você deseja realizar: ") 

print("O operador digitado foi: ", operacao)

valor2 = int(input("Digite o segundo valor da operação: "))

print("O valor digitado foi:", valor2)

if operacao == "+":
    resultado = valor + valor2
    print("O resultado é igual a: ", resultado)

elif operacao == "-":
    resultado = valor - valor2
    print("O resultado é igual a: ", resultado)


elif operacao == "*":
    resultado = valor * valor2
    print("O resultado é igual a: ", resultado)


elif operacao == "/":
    resultado = valor / valor2
    print("O resultado é igual a: ", resultado)

