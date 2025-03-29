def fibonacci(n):
    if n <= 0 or n >= 46:
        print("Por favor, insira um valor de N entre 1 e 45.")
        return

    fib_sequence = [0, 1]  # Início da sequência de Fibonacci
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    
    print(" ".join(map(str, fib_sequence[:n])))

# Solicitar ao usuário o valor de N
try:
    n = int(input("Digite um número inteiro N (N < 46): "))
    fibonacci(n)
except ValueError:
    print("Por favor, insira um número inteiro válido.")
