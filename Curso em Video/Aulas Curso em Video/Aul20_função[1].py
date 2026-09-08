#Cria a função "MostrarLinha"
'''
def MostraLinha():
    print('-' *60)

MostraLinha()
print(f'{'Ola mundo':^50}')
MostraLinha()
MostraLinha()
print(f'{'Despedido':^50}')
MostraLinha()
MostraLinha()
print(f'{'Amor':^50}')
MostraLinha()
MostraLinha()
print(f'{'Hello':^50}')
MostraLinha()
'''
'''
def tit(txt):
    print('=-' * 30)
    print(f'-- {txt} --')
    print('-=' * 30)

tit(str(input('Digite algo para texto:')))
tit
'''
'''
def soma(a, b):
    print(f'A: {a} e B: {b}')
    res = a + b
    print(res)


soma(b= 3, a= 9)
'''
def contador(* num):
    for valor in num:
        print(f'[{valor}]', end=' ')

contador(9,5,3,2,6)
contador(0,3)
contador(8,8,7)