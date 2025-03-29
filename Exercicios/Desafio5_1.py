n = int(input("Digite um número inteiro entra 1 e 45: "))

if n <=0 or n >=46:
    print("Valor inválido")
else:
    fib = [0,1] #Início da sequencia de fibonacci
    for i in range(2,n):
        prox_num = fib[i-1] + fib[i-2]
        fib.append(prox_num)

    print(" ".join(map(str,fib[:n])))

    