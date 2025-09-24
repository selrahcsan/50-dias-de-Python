# **Verificador de Palíndromo:** Desenvolva um programa que verifique se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente).

def verificar(palavra):
    return 'É um palindromo' if palavra == palavra[::-1] else 'Não é um palindromo'

def main():
    palavra = input('Digite uma palavra:\n')
    print(f'A palavra {palavra} é {verificar(palavra)}')

if __name__ == '__main__':
    main()

