# Construa um programa que recebe o número de cadastro (inteiro) de três clientes de uma loja e o valor (em reais) que cada um desses clientes pagou por sua compra. O programa deverá informar:
# (a) o valor total pago pelos três clientes
# (b) o valor da compra média efetuada
# (c) o número de cadastro dos clientes que efetuaram compras superiores a 100 reais
# (d) quantos clientes efetuaram compras inferiores a 50 reais

c1 = int(input("Informe o número de cadastro do primeiro cliente: "))
v1 = float(input("Informe o valor da compra efetuada pelo primeiro cliente: "))
c2 = int(input("Informe o número de cadastro do segundo cliente: "))
v2 = float(input("Informe o valor da compra efetuada pelo segundo cliente: "))
c3 = int(input("Informe o número de cadastro do terceiro cliente: "))
v3 = float(input("Informe o valor da compra efetuada pelo terceiro cliente: "))

vt = v1+ v2+ v3
print("O total pago pelos três clientes é {:2.2f}".format(vt))

media = vt/3
print("O valor da compra média é {:2.2f}".format(media))

print("Cadastro dos clientes que efetuaram compras acima de 100 reais: ")

if v1 > 100:
     print(c1)

if v2 > 100:
  print(c2)

if v3 > 100:
     print(c3)

if v1<100 and v2<100 and v3<100:
    print("0")
     
cont = 0
  
if v1 < 50:
  cont += 1

if v2 < 50:
  cont += 1

if v3 < 50:
  cont += 1

print("A quantidade de clientes que comprou abaixo de 50 reais é ",cont)
