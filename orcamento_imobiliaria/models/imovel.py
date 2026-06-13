class Imovel:
    """
    Classe base do sistema.

    Serve como modelo para
    Apartamento, Casa e Estudio.
    """

    def __init__(self, valor_base):
        self.valor_base = valor_base

    def calcular_aluguel(self):
        raise NotImplementedError(
            "Método deve ser implementado nas subclasses."
        )