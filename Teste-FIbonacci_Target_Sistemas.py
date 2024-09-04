import math

def is_fibonacci(n):
    # Um número é Fibonacci se e apenas se um ou ambos de (5*n^2 + 4) ou (5*n^2 - 4) forem quadrados perfeitos.
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    if n < 0:
        return "Deve ser um número inteiro positivo"
    
    # Checa se n é um Fibonacci
    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        return f"{n} é um número da Sequência de Fibonacci."
    else:
        return f"{n} não é um número da Sequência de Fibonacci."

# Exemplo
while True:
    number = int(input("Entre com um número para checar se ele pertence a Sequência de Fibonacci(insira -1 para encerrar o programa): "))
    if number == -1:
        print("Encerrando o programa")
        break
    print(is_fibonacci(number))
