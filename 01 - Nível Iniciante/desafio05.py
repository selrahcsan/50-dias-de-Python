# Concatenação de Strings: Solicite o nome e o sobrenome do usuário e exiba uma mensagem de boas-vindas com o nome completo.

def saudacao(nome):
    return print(f'Boas Vindas {nome} !')

def main():
    nome = input('Qual o seu nome ?\n')
    saudacao(nome)

if __name__ == '__main__':
    main()    
