# Faça um programa que calcule as seguintes conversões entre sistemas de medida:
# (a) dada uma temperatura na escala Celcius, fornecer a temperatura equivalente em graus
# Farenheit e vice-versa (Fórmula de conversão: F = (9/5) * C + 32
# (b) dada uma medida em polegadas, fornecer a equivalente em milímetros e vice-versa
# (Fórmula de conversão: 1 pol = 25,4 mm)
# O programa deve mostrar uma tela com as quatro conversões de sistema de medida possíveis, perguntando qual deverá ser realizada. Em seguida, deve ler um valor e informá-lo após a conversão como resposta.

a = int(input("Digite 1 se quiser converter um valor de fahrenheit para celsius: \n"
"Digite 2 se quiser converter um valor de celsius para fahrenheit: \n"
"Digite 3 se quiser converter um valor de polegadas para milímetros: \n" 
"Digite 4 se quiser converter um valor de milímetros para polegadas: "))

if a == 1:
    f = float(input("Digite o valor em fahrenheit: ")) 
    c = (f - 32)/(1.8)
    print("O valor correspondente em celsius é: {:2.2f}".format(c))
elif a == 2:
     c = float(input("Digite o valor em celsius: "))
     f = (9/5)*c + 32
     print("O valor correspondente em fahrenheit é: {:2.2f}".format(f))
elif a == 3:
    p = float(input("Digite o valor em polegadas "))
    m = p*25.4
    print("O valor correspondente em milímetro é: {:2.2f}".format(m))
elif a == 4:
    m = float(input("Digite o valor em milímetro "))
    p = m/25.4
    print("O valor correspondente em polegadas é: {:2.2f}".format(p))
