# **Função de Fatorial:** Escreva uma função que calcule o fatorial de um número inteiro não negativo.

num = 0

def fatorial(num):
    return 1 if num <= 1 else num * fatorial(num -1)

def main():
    num = int(input('Digite um número: '))
    print(f'O valor de {num}! é {fatorial(num)}.')

if __name__ == '__main__':
    main()