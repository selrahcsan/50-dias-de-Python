# **Sequência de Fibonacci:** Gere os primeiros N números da sequência de Fibonacci, onde N é informado pelo usuário.

def fibonacci(num):
    fib_sequence = [0, 1]
    while len(fib_sequence) < num:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:num]

def main():
    num = int(input('Informe o Valor desejado:\n'))
    print(fibonacci(num))

if __name__ == '__main__':
    main()

