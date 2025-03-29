#region Tuplas

# Tuplas são "listas" cujos valores após insersão não podem ser alterados como por exemplo uma lista com os dias da semana.

# Para criar uma tupla basta fazer igual uma lista mas ao invés de [] usamos () e separamos os elementos com a ,

print("Tuplas\n")

t = (1,2,3)

# Você também pode variar os tipos de dados
t = ('um',2,'tres',True,4.5,'cinco',False)

print(t)

# Na hora de buscar um dado na tupla em um index específico usamos o [] igual usamos em listas e strings
print(t[2])
print(t[2:5])

# Métodos que funcionam com tuplas

# len() para retornar o tamanho da tupla
print(len(t))

# index() para retornar o em qual índice está um elemento
print(t.index(True))

# count() para retornar quantas vezes um elemento se repete
print(t.count('um'))

#endregion

#region Conjuntos (sets)

# Conjuntos sets são "Listas" mutáveis (Podem ser alterádas) que não podem repetir
# Para criar um conjunto basta criar uma variável e após o sinal de = escrever set()

print("\nConjuntos (sets)\n")

x = set()

# Para adicionar elementos ao conjuto basta usar o método add() e como parâmentro passar o elemento que deseja inserir

x.add(1)
x.add(2)

print(x)

x.add(1)
print(x)

# Todos os métodos vistos na aula de Listas (Aula03) funciona com conjuntos também

#endregion

#region Boolean

#Booleanas

# Boolean são informações que só podem ter dois possíveis valores True, False (Verdadeiro ou Falso),

print("\nBoolean\n")

a = True
b = False

# Os valores booleanos podem ser atribuidos por meio de expressões e comparações
c = 1 < 2
d = 7 > 10

e = None  #Valor nulo

print(a,b,c,d,e)

#endregion

#region Dicionários

# Um dicionário em Python é uma estrutura de dados que armazena pares de chave-valor. Ele permite acesso rápido aos valores a partir de suas respectivas chaves.

# Criando um dicionário simples, use o simbolo de {} após declarar a variável. Um dicionário é uma coleção de pares chave-valor.
meu_dicionario = {
    "nome": "João",  # "nome" é a chave, "João" é o valor
    "idade": 25,     # "idade" é a chave, 25 é o valor
    "cidade": "Belo Horizonte"  # "cidade" é a chave, "Belo Horizonte" é o valor
}

# Acessando valores em um dicionário
# Para acessar um valor, use a chave correspondente:
print(meu_dicionario["nome"])  # Saída: João

# Adicionando uma nova chave-valor ao dicionário
meu_dicionario["profissao"] = "Engenheiro"
print(meu_dicionario)  # Agora inclui "profissao": "Engenheiro"

# Modificando o valor de uma chave existente
meu_dicionario["idade"] = 26  # Atualizamos a idade para 26
print(meu_dicionario["idade"])  # Saída: 26

# Removendo uma chave-valor do dicionário
del meu_dicionario["cidade"]  # Remove a chave "cidade" e seu valor
print(meu_dicionario)

# Iterando sobre um dicionário
# Podemos percorrer todas as chaves ou valores do dicionário:
for chave in meu_dicionario:
    print(f"Chave: {chave}, Valor: {meu_dicionario[chave]}")

# Usando os métodos .keys(), .values(), e .items()
print(meu_dicionario.keys())   # Retorna todas as chaves do dicionário
print(meu_dicionario.values()) # Retorna todos os valores do dicionário
print(meu_dicionario.items())  # Retorna todos os pares chave-valor como tuplas

# Verificando se uma chave existe no dicionário
if "nome" in meu_dicionario:
    print("A chave 'nome' está presente no dicionário!")

# Limpando o dicionário
meu_dicionario.clear()  # Remove todos os itens do dicionário
print(meu_dicionario)  # Saída: {}


#endregion