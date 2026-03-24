#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = n **(1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, d, t, r))