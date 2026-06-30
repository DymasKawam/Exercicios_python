vcasa = float(input('Qual é o valor da casa?:) '))
salario = float(input('Qual é o salário do comprador?: '))
anos = int(input('Quantos anos ele vai pagar?: '))
mes = anos * 12
prestacao = vcasa / mes
if prestacao <= (0.30 * salario):
    print('EMPRESTIMO PERMITIDO')
else:
    print('EMPRESTIMO NEGADO')