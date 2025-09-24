# **Tabuada de Multiplicação:** Peça um número ao usuário e exiba a tabuada de multiplicação desse número de 1 a 10.

def tabuada(num):
    for i in range(11):
        print(f'{num} x {i} = {num * i}')

def main():
    num = int(input('Digite um número:\n'))
    tabuada(num)

if __name__ == '__main__':
    main()
