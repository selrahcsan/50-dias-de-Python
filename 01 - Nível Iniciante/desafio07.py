# **Cálculo de Média:** Peça ao usuário para inserir três notas e calcule a média aritmética.

def media(num1, num2, num3):
    return (num1+num2+num3)/3

def main():
    num1 = int(input('Qual a primeira nota ?\n'))
    num2 = int(input('Qual a segunda nota ?\n'))
    num3 = int(input('Qual a terceira a nota ?\n'))
    print(f'A sua média é {media(num1, num2, num3)}')

if __name__ == '__main__':
    main()
    
