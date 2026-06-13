from models.imovel import Imovel


class Casa(Imovel):

    def __init__(
        self,
        quartos,
        garagem
    ):

        super().__init__(900)

        self.quartos = quartos
        self.garagem = garagem

    def calcular_aluguel(self):

        valor = self.valor_base

        # Acréscimo para 2 quartos
        if self.quartos == 2:
            valor += 250

        # Garagem
        if self.garagem:
            valor += 300

        return valor