# Verificador de Número Par ou Ímpar: Crie um programa que receba um número inteiro e diga se ele é par ou ímpar.

def ehpar(num):
    if num % 2 == 0:
        resultado = 'Par' 
    else:
        resultado = 'Impar'

    return resultado
    
    
def main():
    num = int(input('Digite o número, para saber se é par:\n'))
    resultado = ehpar(num)
    print(f'O {num} é {resultado} !')

if __name__ == "__main__":
    main()


