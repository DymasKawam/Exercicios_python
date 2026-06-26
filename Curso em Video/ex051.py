'Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'
termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termos_sequencia = termo
for c in range (1,11):
    print(termos_sequencia)
    termos_sequencia = termos_sequencia + razao