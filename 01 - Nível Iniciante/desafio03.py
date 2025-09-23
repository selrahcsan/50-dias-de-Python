# Conversor de Unidades (Metros para Centímetros): Peça ao usuário um valor em metros e converta-o para centímetros.

def converter(num):
    return num * 100

def main():
    num = int(input('Digite o valor em cm: '))
    resultado = converter(num)
    print(f'{num}m é igual a {resultado}cm')

if __name__ == '__main__':
    main()

