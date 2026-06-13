from models.imovel import Imovel


class Apartamento(Imovel):

    def __init__(
        self,
        quartos,
        garagem,
        possui_criancas
    ):

        super().__init__(700)

        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):

        valor = self.valor_base

        # Acréscimo para 2 quartos
        if self.quartos == 2:
            valor += 200

        # Garagem
        if self.garagem:
            valor += 300

        # Desconto para quem não possui crianças
        if not self.possui_criancas:
            valor *= 0.95

        return valor