# Calculadora de Idade: Pergunte o ano de nascimento do usuário e calcule a idade aproximada dele.

import datetime

def calculadora_idade(ano_nascimento):
    data = datetime.datetime.now()
    ano = int(data.year)   
    return ano - ano_nascimento 
 
def main():
    ano_nascimento = int(input('Qual o seu ano do seu nascimento? '))
    idade = calculadora_idade(ano_nascimento)
    print(f'A sua idade é {idade}')


if __name__ == '__main__':
    main()
