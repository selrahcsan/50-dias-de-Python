# **Lista de Compras:** Crie um programa que permita ao usuário adicionar e remover itens de uma lista de compras. Ao final, exiba a lista completa.

import os
import sys
import time 

lista_compras = []

def limpar_tela(): 
    _ = os.system('clear') if os.name == 'posix' else os.system('cls')

def continuar():
    print('Continuando em :')
    for i in range(3):
        print(f'{i}')
        time.sleep(0.5)

def adicionar_itens():
    limpar_tela()
    item = input('Qual item deseja adicionar ?\n')
    lista_compras.append(item)
    main()

def remover_itens():
    limpar_tela()
    print(f'{lista_compras}')
    item = input('Qual item deseja remover? \n')
    try:
        lista_compras.remove(item)
        print(f'O item {item} foi removido com sucesso')
    except ValueError:
        print(f'O item {item}, não foi encontrado na lista! ')

    continuar()
    main()

def exibir_lista():
    limpar_tela()
    print('Sua Lista de Compras')
    
    for itens in lista_compras:
        print(f'-> {itens}')
    
    continuar()
    
def opcao_menu(opcao):
    if opcao == '1':
        adicionar_itens()
    if opcao == '2':
        remover_itens()
    if opcao == '3':
        exibir_lista()
    if opcao == '4':
        limpar_tela()
        sys.exit()
    else:
        print('Opção Invalida')
        main()

def main():
    limpar_tela()   
    print('--Lista de Compras--\n')
    print('[1] Adicionar Itens')
    print('[2] Remover Itens')
    print('[3] Exibir Lista')
    print('[4] Sair\n')
    opcao = input('Opção: ')
    opcao_menu(opcao)
    
if __name__ == '__main__':
    main()
