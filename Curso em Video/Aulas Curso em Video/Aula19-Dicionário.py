#Dicionários são estruturas de dados semelhantes a tuplas e listas, mas com a diferença de que os elementos são armazenados em pares de chave e valor. 

#exemplo = {'nome': 'Gustavo', 'idade': 22, 'sexo': 'M'}

'''
print(exemplo['nome'])
print(exemplo['idade'])
print(exemplo['sexo']) 
'''
#para adicionar valores:
'''
exemplo['tamanho'] = 1.78

print(exemplo['tamanho'])
'''

#para excluir valores

'''
del exemplo['idade']

print(exemplo)
'''

filmes = {
'Titulo': 'StarWars',
'Ano': 1977,
'diretor': 'George Lucas',
}

#para pegar as valores do dicionário filme eu posso usar o :
'''
print(filmes.values())
'''

#para pegar as chaves eu posso usar:
'''
print(filmes.keys())
'''

#para pegar os dois eu posso usar:
'''
print(filmes.items())
'''

'''
for k, v in filmes.items():
    print(f'O {k} é {v}')
'''

#também da para juntar Lista com Dicionários
#exemplo

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''

#============================
estado = {}
brasil = []
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().title()
    estado['sigla'] = str(input('sigla do estado: ')).strip().upper()
    brasil.append(estado.copy())
print(brasil)
for i in brasil:
    for k, v in i.items():
        print(f'O campo {k} tem valor {v}')