# Faça um programa que converta um número inteiro positivo para a notação de números romanos, considerando os seguintes símbolos romanos: I, V, X, L, C, D, M.

v = int(input("Informe o valor a ser convertido em algarismos romanos: "))

mr = ["","M","MM","MMM"]
cr = ["","C","CC","CD","D","DC","DCC","DCCC","CM"]
dr = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
ur = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

mc = mr[v // 1000]
cc = cr[(v % 1000) // 100]
dc = dr[(v % 100) // 10]
uc = ur[(v % 10)]

t = mc + cc + dc + uc

print("Valor convertido: ", t)
