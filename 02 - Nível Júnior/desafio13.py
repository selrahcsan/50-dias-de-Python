# **Inversor de Palavras:** Escreva uma função que receba uma string e a retorne invertida. Ex: "python" -> "nohtyp".

def inverter(palavra):
    return palavra[::-1]

def main():
    palavra = input('Escreva uma palavra:\n')
    print(f'A {palavra} invertida, fica {inverter(palavra)}')

if __name__ == '__main__':
    main()
