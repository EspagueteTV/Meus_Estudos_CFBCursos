class Carro:
    velMax = 0
    ligado = False
    cor = ""


c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.cor = "Preto"
c1.ligado = False


print(f"Velocidade Máxima: {c1.velMax} Km/h")
print(f"Cor: {c1.cor}")
estado = 'sim' if c1.ligado else 'nao'

print(f"Ligado: {estado}")
