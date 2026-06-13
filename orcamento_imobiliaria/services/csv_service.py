import csv


def gerar_csv(valor_mensal):

    with open(
        "parcelas_orcamento.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow(
            ["Mês", "Valor"]
        )

        for mes in range(1, 13):

            writer.writerow(
                [
                    mes,
                    f"R$ {valor_mensal:.2f}"
                ]
            )

    print(
        "\nArquivo CSV gerado com sucesso."
    )