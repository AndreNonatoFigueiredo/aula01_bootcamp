# Desafio Aula 1

# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu.
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
percentual_bonus = float(input("Digite o percentual do seu bônus: "))

bonus = salario * (percentual_bonus) + 1000

print("Olá, " + nome + ". O seu bônus foi de "+  str(bonus))
1