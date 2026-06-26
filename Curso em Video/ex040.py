n1 = float(input('Digite sua Primeira nota: '))
n2 = float(input('Digite sua Segundo nota:'))
média = (n1 + n2) / 2
if média < 5:
    print('Reprovado')
elif média >= 5 and média < 6.9:
    print('Recuperação')
else:
    print('Aprovado')