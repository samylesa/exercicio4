class Carros(object):
    def __init__(self, consumo, gasolina=0):
        self.consumo = consumo
        self.gasolina = gasolina

    def adicionarGasolina(self, adicionar):
        self.gasolina = self.gasolina + adicionar

    def andar(self, quilometros):
        self.gasolina = self.gasolina - (quilometros/self.consumo)

    def obterGasolina(self):
        return self.gasolina



    
