class Contrato:

    VALOR_CONTRATO = 2000

    @staticmethod
    def calcular_parcelamento(parcelas):

        if parcelas < 1 or parcelas > 5:

            raise ValueError(
                "O parcelamento deve ser entre 1 e 5 vezes."
            )

        return Contrato.VALOR_CONTRATO / parcelas