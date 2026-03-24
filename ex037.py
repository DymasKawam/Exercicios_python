n1 = int(input('Digite um número qualquer: '))
print('Escolha uma das bases para conversão:')
print('[1] converter para BINÁRIO.')
print('[2] converter para OCTAL.')
print('[3] converter para HEXADECIMAL.')
escolha = int(input('Qual você escolhe?: '))
if escolha == 1:
    print('{} convertido para binário é igual a {}.'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}.'.format(n1, oct(n1) [2:]))
elif escolha == 3:
    print('{} convertido para octal é igual a {}.'.format(n1, hex(n1) [2:]))
else:
    print('Você inseriu um número que não está nas opção.')