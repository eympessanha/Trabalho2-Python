# Escreva um programa para ler os valores das coordenadas cartesianas de um ponto e imprimir os valores lidos, seguidos do número (1 a 4) do quadrante em que o ponto está situado. Se o ponto estiver situado sobre um dos eixos, fornecer o valor -1. Se estiver sobre a origem, fornecer o valor 0.

x = float(input("Informe o valor X da coordenada cartesiana: "))
y = float(input("Informe o valor Y da coordenada cartesiana: "))

print("Valor de X: ",x,"\nValor de Y: ",y)

if x > 0 and y > 0:
   print("Quadrante 1")
elif x > 0 and y < 0:
   print("Quadrante 4")
elif x < 0 and y < 0:
   print("Quadrante 3")
elif x < 0 and y > 0:
   print("Quadrante 2")
elif (x == 0 and y != 0) or (x != 0 and y == 0):
   print("Valor -1")
elif x == 0 and y == 0:
   print("Valor 0")
