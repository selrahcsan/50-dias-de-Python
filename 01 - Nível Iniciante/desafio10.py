#  **Calculadora de Área de um Quadrado:** Solicite o lado de um quadrado e calcule sua área e seu perímetro.

def area(lado):  
    return lado ** 2

def perimetro(lado):
    return 4 * lado

def main():
    lado = int(input('Digite o valor do lado de um quadrado:\n'))
    print(f'Áera: {area(lado)}\nPerímetro: {perimetro(lado)} ')

if __name__ == '__main__':
    main()
