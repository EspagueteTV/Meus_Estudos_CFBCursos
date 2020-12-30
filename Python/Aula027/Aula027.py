import os
from time import sleep

carros = list()

class Carro:
    nome = ""
    potencia = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.potencia = int(pot)
        self.velMax = int(pow(self.potencia, 2))

    def ligar(self):
        self.ligado = True

    def dsligar(self):
        self.ligado = False

    def info(self):
        print(f"Nome.............: {self.nome}" )
        print(f"Potência.........: {self.potencia}")
        print(f"Velocidade Máxima: {self.velMax}")
        print(f"Ligado...........: {'Sim' if self.ligado else 'Não'}")

def menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair do Programa")
    print("Quantidadde de carros: " + str(len(carros)))
    print("-=" * 20)
    opc = int(input("Digite uma opção: "))
    return opc


def NovoCarro():
    os.system("cls") or None
    n = str(input("Digite o nome do carro: "))
    p = int(input("Potência do carro.....: "))
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro criado com sucesso")
    sleep(2)


def Informacoes():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja ter as informações: "))
    try:
        carros[n].info()
    except:
        print("Carro não existe na lista")
    sleep(2)

def ExcluirCarro():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja excluir: "))
    try:
        del carros[n]
    except:
        print("Carro não existe na lista  ")
    sleep(2)


def Ligar():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja ligar: "))
    try:
        carros[n].ligar()
        print(f"Carro {n} ligado")
    except:
        print("Carro não existe na lista")

def Desligar():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja desligar: "))
    try:
        carros[n].desligar()
        print(f"Carro {n} desligado")
    except:
        print("Carro não existe na lista")
    sleep(2)


def Listar():
    os.system("cls") or None
    p = 0
    for c in carros:
        print(f"{p} - {c.nome}")
        p += 1
    sleep(2)


ret = menu()
while ret < 7 and ret > 0:
    if ret == 1:
        NovoCarro()
    elif ret == 2:
        Informacoes()
    elif ret == 3:
        ExcluirCarro()
    elif ret == 4:
        Ligar()
    elif ret == 5:
        Desligar()
    elif ret == 6:
        Listar()
    elif ret == 7:
        break
    ret = menu()

os.system("cls")
print("Programa finalizado com sucesso.")





