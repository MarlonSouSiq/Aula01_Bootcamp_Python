nome = input("Entre com o seu nome: ")
salario = float(input("Entre com o seu salario: "))
porcentagem = float(input("porcentagem do bonus: "))

valor= float(salario*porcentagem + salario)

print(f"Parabens, {nome}. O seu salario deste mes com bonus sera: R$ {valor:.2f}")

#print(" Parabens ", nome, " O valor do seu salario com bonus ser: R$ ",valor)

