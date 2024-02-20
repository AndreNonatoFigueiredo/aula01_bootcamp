nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
percentual_bonus = float(input("Digite o percentual do seu bônus: "))

bonus = salario * (percentual_bonus) + 1000

print("Olá, " + nome + ". O seu bônus foi de "+  str(bonus))
