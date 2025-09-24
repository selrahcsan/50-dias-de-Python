# **Contador de Vogais:** Crie um programa que conte o número de vogais em uma string fornecida pelo usuário.

def contador_vogais(frase):
    vogais = 'aeiou'
    contador = 1

    for caracteres in frase.lower():
        if caracteres in vogais:
            contador +=1

    return contador

def main():
    frase = input('Digite uma frase:\n')
    print(f'Sua frase, tem {contador_vogais(frase)} vogais')

if __name__ == '__main__':
        main()
