# Ler dois valores inteiros para as variáveis A e B. Efetuar a troca dos
# valores de forma que a variável A passe a possuir o valor da variável B e a
# variável B passe a possuir o valor da variável A. Apresentar os valores
# trocados.
A = float(input('Informe o número A'))
B = float(input('Informe o número B'))
A, B = B, A
print('resultado',A,B)

