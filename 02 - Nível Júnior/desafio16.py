#  **Encontrando o Maior Número:** Escreva   uma função que receba uma lista de números e retorne o maior valor.

numero = []

def maior(numero):
    return max(numero)

def main():
    tamanho = int(input('Tamanho da lista\n'))

    for posicao in range(tamanho):
        num = int(input(f'Digite o número [{posicao+1}]: '))
        numero.append(num)

    print(f'O maior número {maior(numero)}')
        
if __name__ == '__main__':
    main()
