# Faça um programa que leia a temperatura em graus Celsius e apresente
# convertida em graus Fahrenheit. A fórmula de conversão é:
# F = (9*C + 160)/5
# Sendo F a temperatura em c e C a temperatura em Celsius.
# }
temperaturacelsius= float(input('informe a temperatura em celcius'))
fahrenheit = (9*temperaturacelsius + 160)/5
print('temperatura em fahrenheit', fahrenheit)
