# **Adivinhe o Número:** Crie um jogo simples onde o computador "pensa" em um número entre 1 e 100 
# e o usuário tem que adivinhar. O programa deve dar dicas (maior/menor).

import random

def verifica(num):
    if num > numero_computador:
        print('Eu escolhi um numero menor')
    elif num < numero_computador:
        print('Eu escolhi um número Maior')

def main():
    global numero_computador 
    numero_computador = random.randint(1,100)
    num = int(input('Digite um número entre 1 e 100\n:'))
    while num != numero_computador:
        verifica(num)
        num = int(input('Digite um número entre 1 e 100\n'))
    print('Parabéns, Vc acertou!')

if __name__ == '__main__':
    main()