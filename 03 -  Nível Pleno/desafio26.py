# **Classe Carro:** Crie uma classe chamada Carro com os atributos marca, modelo e ano. Adicione métodos para ligar(), desligar() e acelerar().

import time

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print(f'O {self.marca} {self.modelo} já está ligado.')
        else:
            self.ligado = True
            print(f'O {self.marca} {self.modelo} foi ligado. VRUMM!!!!')

    def desligar(self):
        if not self.ligado:
            print(f'O {self.marca} {self.modelo} já está desligado.')
        else:
            self.ligado = False
            print(f'O {self.marca} {self.modelo} foi desligado. Poff.')

    def estado(self):
        status = 'ligado' if self.ligado else 'desligado'
        print(f'O {self.marca} {self.modelo} ({self.cor}) está atualmente {status}.')


def main():
    marca = input('Qual a marca do seu carro ?\n')
    modelo = input(f'Qual é o modelo do seu {marca}:\n')
    cor = input(f'Qual é a cor do seu {modelo}:\n')
    meu_carro = Carro(marca, modelo, cor)     

    meu_carro.estado()
    time.sleep(1)
    meu_carro.ligar()
    time.sleep(1)
    meu_carro.estado()
    time.sleep(1)
    meu_carro.desligar()
    time.sleep(1)
    meu_carro.estado()


if __name__ == '__main__':
    main()

