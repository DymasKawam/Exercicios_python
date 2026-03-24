print('-=' * 50)
print('Analisador de triângulos')
print('-=' * 50)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o Terceiro segmento: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('Esses segmentos PODEM formar um triângulo.')
else: 
    print('Esses segmento NÃO podem formar um triângulo.')