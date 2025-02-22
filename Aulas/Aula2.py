# Strings → Textos (→ = alt + 26)

#uma palavra
string1 = "Oi!"

#uma frase
string2 = "Oi, tudo bem?"

#com aspas únicas
string3 = 'Ctrl+Play - escola de progamação e robótica'
'''
print(string1)
print(string2)
print(string3)
'''
#para saltar linhas basta usar o comando \n
#print('Olá mundo!\nSejam bem-vindos')

# função len() → verifica o quantidade de caracteres

print(len(string3))

#region index
'''
#Index → representado pelo simbolo []

nome = 'Pedro Paulo Sousa do Couto'

print(nome[0])

#imprimir a partir de um caractere
print(nome[5:])

print(nome[:5])

#imprimir parte de um string
print(nome[0:12])

#imprimir inverso
print(nome[-1])

print(nome[:-1])

#imprime uma frase saltando letras
print(nome[::2])
'''
#endregion

#função find() serve para encontrar em qual posição está o caractere específico

email = 'fulano@ctrlplay.com.br'

print(email.find('@'))
pos = email.find('@')
print(email[:pos])

#função count() serve para contar quantas vezes um caractere se repetiu na string

print(email.count('.'))

#string são imutáveis, você não pode pegar uma string e alterar um valor no index

'''
teste = 'Pedro'
teste[3] = 'l'
'''

#region Operadores em String
#concatenação (+)
nome = 'José'
sobrenome = 'Bond'
print(nome+sobrenome)

#repetição
print(nome*5)

#conversão para string

media = 6.5
print('A média do '+nome+' foi de '+ str(media))
print('A média do',nome,'foi de',media)
#endregion

#region Métodos de String

exemplo = "Ctrl+Play - Escola de Programação e Robótica"

#Coloca tudo em maiusculo
print(exemplo.upper())

#Coloca tudo minúsculo
print(exemplo.lower())

#Divide a string nos espaços em branco
cadaPalavra = exemplo.split()
print(cadaPalavra)
print(cadaPalavra[2])

#divide em um elemento específico (não inclui o elemento que foi dividido)
cadaPalavra = exemplo.split('-')
print(cadaPalavra)
print(cadaPalavra[1])

#endregion

nome = input("Digite seu nome: ")
print("\nOlá "+nome)


