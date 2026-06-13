from models.imovel import Imovel


class Estudio(Imovel):

    def __init__(self, vagas):

        super().__init__(1200)

        self.vagas = vagas

    def calcular_aluguel(self):

        valor = self.valor_base

        if self.vagas >= 2:

            valor += 250

            vagas_extras = self.vagas - 2

            if vagas_extras > 0:
                valor += vagas_extras * 60

        return valor