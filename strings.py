nome = input('Digite seu nome: ')
idade = input('digite sua idade: ')
tamanho = len(nome)

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome contém {tamanho} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
# elif nome or idade:
#    print('Desculpas, deixou campos vazios')
else:
    pass

if ' ' in nome:
    print(f'Seu nome possui espaços')
else:
    print(f' Seu nome não possui espaços')


if nome or idade:
    print(f'Campos vazios')
else:
    pass
