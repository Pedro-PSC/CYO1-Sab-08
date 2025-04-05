#region Cidade e Pais
print('Exercício 1 - Cidade e País\n')

def Cidade_Pais(cidade:str,pais:str='Brasil'):
    print(f'{cidade} está localizado no {pais}')

Cidade_Pais('Belo Horizonte')
Cidade_Pais('Lagoa Santa')
Cidade_Pais('Paris','França')

print('\n')
#endregion

#region Quem é mais rápido

def Velocidade(distancia:float,tempo:float):
    v = distancia/tempo
    return v

def Conversor(tempo_60):
    # Converte o tempo de base 60 para base 100
    inteiro = int(tempo_60)  # Parte inteira do tempo (horas ou minutos inteiros)
    decimal = tempo_60 - inteiro  # Parte decimal representando frações de minutos
    decimos = int(decimal * 60)  # Converte a parte decimal em minutos
    tempo_100 = inteiro * 100 + (decimos * 100 // 60)
    return tempo_100

def MaisRapido():
    op = int(input("Como deseja fazer a operação:\n1 → Km/h\n2 → m/s\nInsira aqui: "))
    op = 'Km/h' if op == 1 else 'm/s'

    dist = float(input("Digite a distância percorrida por ambos: "))
    print(f'A distância inserida foi de: {dist} {op}\n')

    print('Insira o tempo de percurso da seguinte forma Ex.: 2.3 → 2 horas e 30 minutos ou 2 minutos e 30 segundos\n')
    tempo1 = float(input("Tempo de percurso do primeiro corredor: "))
    tempo2 = float(input("Tempo de percurso do segundo corredor: "))

    new_tempo1 = Conversor(tempo1)
    new_tempo2 = Conversor(tempo2)

    vel1 = Velocidade(dist,new_tempo1)
    vel2 = Velocidade(dist,new_tempo2)

    if (vel1 > vel2):
        print(f'\nO segundo corredor foi o mais rápido, fazendo o percurso com velocidade de {new_tempo2} {op} e o primeiro em {new_tempo1} {op}')
    else:
        print(f'\nO primeiro corredor foi o mais rápido, fazendo o percurso com velocidade de {new_tempo1} {op} e o segundo em {new_tempo2} {op}')

MaisRapido()
#endregion