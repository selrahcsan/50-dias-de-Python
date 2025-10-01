# **Agenda de Contatos Simples:** Crie um dicionário para armazenar nomes e números de telefone. Permita que o usuário adicione e procure por contatos.

import sys 

agenda = {}

def adicionar_contato():
    nome = input('Digite o nome:\n')
    celular = input('Celular:\n')
    agenda[nome] = celular
    print(f'Contato {nome} adicionado !')
    

def remover_contato():
    contato = input('Digite o nome do contato a ser removido:\n')
    if contato in agenda:
        del agenda[contato]
        print('Contato removido!\n')
    else:
        print('Contato não encontrado\n')

def exibir_agenda():
    if agenda:
        print('\n-- Lisya de Contatos')
        for nome, celular in agenda.items():
            print(f'{nome} -> {celular}')
    else:
        print('Agenda Vazia')

def sair():
    sys.exit()

opcoes = {
        '1': adicionar_contato,
        '2': remover_contato,
        '3': exibir_agenda,
        '4': sair
}

def opcao_menu(opcao):
    funcao = opcoes.get(opcao)
    funcao() if funcao else print('Opção Inválida')
    main()
    

def main():
    print('''-- Agenda Simples --
    [1] Adicionar Contato
    [2] Remover Contato
    [3] Listar Contatos
    [4] Sair
    ''')
    escolha = input('Opção: ')
    opcao_menu(escolha)


if __name__ == '__main__':
    main()

  
