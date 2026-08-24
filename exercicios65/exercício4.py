'''
Ler quatro valores numéricos inteiros e apresentar o resultado dois a dois da adição e multiplicação entre os  valores lidos, baseando-se na utilização do conceito de propriedade distributiva. Dica: se forem lidas as variáveis  A, B, C e D, devem ser somados e multiplicados os valores de A com B, A com C e A com D; depois B com C, B  com D e por último C com D. Note que para cada operação serão utilizadas seis combinações. Assim sendo,  devem ser realizadas doze operações de processamento, sendo seis para as adições e seis para as  multiplicações. 
 '''
cont= 0
soma = []
multi = []

números = [int(input('número A: ')),int(input('número B: ')),int(input('número C: ')),int(input('número D: ')) ]

for i in range (0,3):
    for c in range(0, 4):
        if  c <= i:
            continue
        adi = números[i] + números[c]
        mut = números[i] * números[c]
        soma.append(adi)
        multi.append(mut)
print('-=' * 30)
print(f'{'ADIÇÃO':>30}')
for i in range(0, 3):
    for c in range(0,4):
        if c <= i:
            continue
        else:
            print(f'[{números[i]} + {números[c]} = {soma[cont]}]', end=' ')
            cont+= 1
    print()

cont = 0
print('-='*30)
print(f'{'MULTIPLICAÇÃO':>35}')
for i in range (0,3):
    for c in range(0,4):
        if c <= i:
            continue
        else:
            print(f'[{números[i]} * {números[c]} = {multi[cont]}]', end=' ')
            cont += 1
    print()