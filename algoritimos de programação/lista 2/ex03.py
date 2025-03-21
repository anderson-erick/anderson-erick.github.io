ve = int(input('Informe o valor do empréstimo'))
p = int(input('Informe o número de parcelas'))
s = int(input('Informe o seu salário'))
emprestimo = ve / p

if emprestimo > s*0.3:
    print ('Empréstimo aprovado')
else: 
    print ('Empréstimo rejeitado')