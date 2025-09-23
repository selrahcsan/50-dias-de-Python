#  **Soma Simples:** Crie um programa que solicite dois números ao usuário e mostre a soma deles.

def soma(num1, num2):
    return num1 + num2

def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número'))
    resultado = soma(num1, num2)
    print(f'R: {num1} + {num2} = {resultado}')

if __name__ == '__main__':
    main()
   
