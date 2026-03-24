#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
Me = float(input('Digite um valor em metros: '))
Ce = Me * 100
Mi = Ce * 100
print('Convertendo {} para Centímetros é {} e para Milímetros é {}'.format(Me, Ce, Mi))