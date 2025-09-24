# **Manipulação de Strings (Maiúsculas e Minúsculas):** Receba uma palavra do usuário e imprima-a em maiúsculas e minúsculas.

def maiuscula(palavra):
    return palavra.upper()

def minuscula(palavra):
    return palavra.lower()

def main():
    palavra = input('Informe uma Palavra:\n')
    print (f'A palavra {palavra} em :\nmaiuscula: {maiuscula(palavra)}\nminuscula: {minuscula(palavra)}')

if __name__ == '__main__':
    main()
