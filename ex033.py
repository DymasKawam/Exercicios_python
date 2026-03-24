a = int(input('Digite um valor: '))
b = int(input('Digite um outro valor: '))
c = int(input('Digite um outro valor: '))
#menor número
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('menor número foi {}'.format(menor))
#Maior número
maior = b 
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print('Menor número foi {}'.format(maior))