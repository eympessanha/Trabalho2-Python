# Escreva um programa que leia o salário fixo de um vendedor de uma loja e o valor total de vendas efetuadas por ele no mês. Acrescente ao salário um prêmio, conforme as condições a seguir:
# Total de Vendas = 1000 < v ≤ 5000 -> Premio = 500,00
# Total de Vendas = 5000 < v ≤ 7500 -> Premio = 700,00
# Total de Vendas = v > 7500 -> Premio = 1000,00
# O programa deve calcular e informar o salario final do vendedor e qual foi o prêmio recebido.

s =float(input("Digite o salário fixo: "))
v =  float(input("Digite o valor total de vendas efetuadas no mês: "))

if 1000<v<=5000:
  p = 500
  t = s+p
  print("O salário final é {:2.2f}".format(t))
  print("O valor do prêmio é {:2.2f}".format(p))
elif 5000<v<=7500:
  p = 700
  t = s+p
  print("O salário final é {:2.2f}".format(t))
  print("O valor do prêmio é {:2.2f}".format(p))
else:
  p = 1000
  t = s+p
  print("O salário final é {:2.2f}".format(t))
  print("O valor do prêmio é {:2.2f}".format(p))
