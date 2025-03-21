#Elaborar um programa que calcule e apresente o volume de uma caixa
#retangular, por meio da fórmula:
#volume = comprimento * largura * altura
comprimento = float(input('Informe o comprimento'))
largura = float(input('Informe a latgura'))
altura = float(input('Informe a altura'))
#calculando o volume
volume = comprimento*largura*altura
print(f'Volume {volume:.2f}')

