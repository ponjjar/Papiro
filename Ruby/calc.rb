puts "Digite o primeiro numero"
primeiroNumero = gets.chomp.to_i
puts "Digite o segundo numero"
segundoNumero = gets.chomp.to_i

puts "Escolha uma das opções abaixo:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
"    

opcao = gets.chomp.to_i

case opcao
when 1
    puts "A soma dos numeros é #{primeiroNumero + segundoNumero}"
when 2
    puts "A subtração dos numeros é #{primeiroNumero - segundoNumero}"
when 3
    puts "A multiplicação dos numeros é #{primeiroNumero * segundoNumero}"
when 4
    puts "A divisão dos numeros é #{primeiroNumero / segundoNumero}"
else
    puts "Opção invalida"
end
