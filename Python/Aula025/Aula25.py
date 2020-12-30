class NPC: #SuperClasse, classe pai

    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f'Nome...: {self.nome}')
        print(f'Time...: {self.time}')
        print(f'Força..: {self.forca}')
        print(f'Munição: {self.municao}')
        print(f'Vivo...: {"Sim" if self.vivo else "Não"}')
        print(f'Energia: {self.energia}')
        print('-=' * 20)

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)


class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)




class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)

    def inf(self):
        super().info()


s1 = Guarda('Olho Vivo', 1)
s2 = Soldado('Bala na Agulha', 2)
s3 = Elite('Ninja', 1)
s4 = Guarda('Super Atento', 2)
s5 = Soldado('Tiro Certo', 2)
s6 = Elite('Samurai', 2)

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()

