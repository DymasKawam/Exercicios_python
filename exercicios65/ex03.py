loja = []
cont = 0
while True:
    vendedor = str(input('Digite o nome do vendedor: ')).strip().title()
    peça = str(input('Digite o produto: ')).strip().title()
    preço = float(input('Digite o preço do produto: R$'))
    quant = int(input('Digite a quantidade vendida: '))
    com = (preço * quant) * (5 / 100)
    loja.append([vendedor,peça,preço,quant,com])
    
    continuar = str(input('Deseja continuar?[S/N]: ')).strip()
    if continuar in 'Nn':
        break
print(f'{'Tabela De vendedores':^70}')
print(f'{'Vendedor':<20}{'peça':<10}{'preço':<10}{'quantidade':<15}{'comição':<10}')
print('-=' * 35)
for v in loja:
    print(f'{v[0]:<20}{v[1]:<10} R${v[2]:<10}{v[3]:<15}{v[4]:<10.2f}')