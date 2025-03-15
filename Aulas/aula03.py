#region Criação, Adição e Remoção de Lista

# Para criar uma lista em pythom basta declarar um nome e após o = usar o simbolo de colchetes

convidados = ['Pedro','Lucas','Sebastian','Júlia','Leonan','Magnum']
print(convidados)

#os índices em pythom basta colocar o valor dentro de []
print('Primeiro convidado da festa: '+convidados[0])
print('Penúltimo convidado da festa: '+convidados[-2])

#Substituindo o primeiro item
convidados[0] = "Isabella"
print(convidados)

#adicionando um item na lista (Todo item adicionado na lista sempre irá pro final da lista)
convidados.append("Pedro")
print(convidados)

#Se eu quiser adicionar em um local específico da lista
convidados.insert(2,"Antônio")
print(convidados)

#eliminar item da lista
del convidados[2]
print(convidados)

#exclui o item lista mas salva em uma variável
convidadoRemovido = convidados.pop()
print(convidados)
print(convidadoRemovido)

convidadoRemovido = convidados.pop(0)
print(convidados)
print(convidadoRemovido)

#exclui por um item específico
viajando = 'Leonan'
convidados.remove(viajando)
print(convidados)
print(viajando+' não vai a festa, pois está viajando')

#endregion

#region Organizando item na lista

#sorted() → ele organiza a lista em ordem alfabética apenas para exibição
print(sorted(convidados))
print(sorted(convidados,reverse=True))
print(convidados)

#sort() → ele organiza a lista em ordem alfabética porém de fato altera a lista
#convidados.sort()
print(convidados)
#para fazer invertido basta colocar reverse=True dentro do ()

#reverse() → Inverte a lista sem organizar em orgem alfabética
convidados.reverse()
print(convidados)

#endregion

#region Funções úteis

#exibir o tamanho de uma lista
print(len(convidados))

#criar uma lista de números
numeros = list(range(1,5))
print(numeros)

#menor valor
print(min(numeros))

#maior valor
print(max(numeros))

#fatia de uma lista
print(convidados[1:3])

#para copiar uma lista
convidados2 = convidados[:]
print(convidados2)

#endregion

#region Matrizes

timesXpessoas = [["Palmeiras","Flamengo","Sport","Galo","Cruzeiro"],["José","Maria","Tiago","Lucas","Luana"]]

print(timesXpessoas)

#Para Exibir uma lista específica
print(timesXpessoas[0])
print(timesXpessoas[1])

#Para exibir um item de uma lista específica
print(timesXpessoas[0][3])
print(timesXpessoas[1][3])

#endregion