# DIA 1 - Exercícios básicos de Python

# Primeiros testes com print
print("Olá, mundo!")
print(7 + 4)             # Soma de dois números
print('7' + '4')         # Junção de duas strings (concatenação)
print('ola,5')           # Apenas uma string simples

# Coletando dados do usuário
nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
peso = input('Qual é o seu peso? ')

# Exibindo os dados formatados
print('Olá', nome, 'você tem', idade, 'anos e pesa', peso, 'kg.')

# Coletando data de nascimento
dia = input('Qual dia você nasceu? ')
mes = input('Qual mês você nasceu? ')
ano = input('Qual ano você nasceu? ')

# Mostrando a data com formatação
print('Você nasceu no dia', dia, 'de', mes, 'de', ano + '. Correto?')

# Soma de dois números inteiros
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('A soma é =', n1 + n2)

# Cálculo de idade futura
nome = input('Qual é o seu nome? ')
n1 = int(input('Em que ano você nasceu? '))
print(nome, 'em 2025 você terá', 2025 - n1, 'anos.')
