# 1. Soma da sequência de Fibonacci:
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > n:
            break
        fib_sequence.append(next_value)
    return fib_sequence

def pertence_a_fibonacci(num):
    if num < 0:
        return False
    sequence = fibonacci_sequence(num)
    return num in sequence


# Entrada do usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verificação
if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")