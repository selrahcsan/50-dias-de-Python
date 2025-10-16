#  **Operações Matemáticas:** Peça dois números e exiba o resultado da soma, subtração, multiplicação e divisão.

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return 'Divisão por zero'
    else:
        return num1 / num2

def main():
    num1 = int(input('Qual o primeiro Número:\n'))
    num2 = int(input('Qual o segundo número:\n'))

    print(f'{num1} + {num2} = {soma(num1, num2)}')
    print(f'{num1} - {num2} = {subtracao(num1, num2)}')
    print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')
    print(f'{num1} / {num2} = {divisao(num1, num2)}')

if __name__ == '__main__':
    main()

