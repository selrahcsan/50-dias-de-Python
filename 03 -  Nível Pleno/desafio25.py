#  **Gerador de Senhas Aleatórias:** Crie uma função que gere uma senha aleatória com um comprimento específico, contendo letras maiúsculas, minúsculas, números e símbolos.

import string
import secrets

def gerar_senha(tamanho):
    if tamanho < 8:
        return 'Deve ter um tamanho maior que 8'
    
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation
    
    caracteres = letras_maiusculas + letras_minusculas + digitos + simbolos
    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho))

    return senha


    
def main():
    num = int(input('Digite o Tamanho da senha (>8):\n'))
    print(f'Senha gerada é : {gerar_senha(num)}')

if __name__ == '__main__':
    main()

