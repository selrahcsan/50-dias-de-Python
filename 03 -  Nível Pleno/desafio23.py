#  **** Use list comprehension para criar uma lista de todos os números entre 1 e 100 que são divisíveis por 7.

def listar():
    num = [i for i in range(1,101) if i % 7 == 0]
    return num

def main():
    print('Lista de Número de 1 a 100, que são divisíveis por 7!')
    print(listar())

if __name__ == '__main__':
    main()
