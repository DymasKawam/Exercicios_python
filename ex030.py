numero = int(input('Me fale um número qualquer: '))
par = numero % 2
if par == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))