# **Filtrando Números Pares:** Crie uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.

import random

def eh_par(num):
    return True if num % 2 == 0 else False
    
def lista_par():
    for i in num:
        if eh_par(i):
            print(i, end=' ')

def gera_num_aleatorios():
    cont = 0
    while cont < 20:
        num_random = random.randint(1,20)
        num.append(num_random)
        cont += 1

def main():
    global num
    num = [ ]
    gera_num_aleatorios()
    print(f'A lista gerada foi:\n{num}\nEsse são os numeros pares:')
    lista_par()
    print()

if __name__ == '__main__':
    main()

