#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
nI = int(input('Digite um número: '))
s = nI + 1
an = nI - 1
print('Depois do {} vem {} e antes do {} vem {}'.format(nI, s, nI, an))