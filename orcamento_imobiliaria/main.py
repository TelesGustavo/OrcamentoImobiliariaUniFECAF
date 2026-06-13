from models.apartamento import Apartamento
from models.casa import Casa
from models.estudio import Estudio

from services.contrato import Contrato
from services.csv_service import gerar_csv


# Função para ler números inteiros
def ler_inteiro(mensagem):

    while True:

        try:

            return int(input(mensagem))

        except ValueError:

            print(
                "Digite apenas números."
            )


# Função para validar S ou N
def ler_sim_nao(mensagem):

    while True:

        resposta = input(
            mensagem
        ).strip().lower()

        if resposta in ["s", "n"]:

            return resposta == "s"

        print(
            "Digite apenas S ou N."
        )


print("=" * 50)
print("SISTEMA DE ORÇAMENTO IMOBILIÁRIO R.M")
print("=" * 50)

print("\n1 - Apartamento")
print("2 - Casa")
print("3 - Estúdio")


while True:

    tipo = ler_inteiro(
        "\nEscolha uma opção: "
    )

    if tipo in [1, 2, 3]:
        break

    print("Opção inválida.")


if tipo == 1:

    quartos = ler_inteiro(
        "Quantidade de quartos (1 ou 2): "
    )

    garagem = ler_sim_nao(
        "Possui garagem? (S/N): "
    )

    criancas = ler_sim_nao(
        "Possui crianças? (S/N): "
    )

    imovel = Apartamento(
        quartos,
        garagem,
        criancas
    )

elif tipo == 2:

    quartos = ler_inteiro(
        "Quantidade de quartos (1 ou 2): "
    )

    garagem = ler_sim_nao(
        "Possui garagem? (S/N): "
    )

    imovel = Casa(
        quartos,
        garagem
    )

else:

    vagas = ler_inteiro(
        "Quantidade de vagas: "
    )

    imovel = Estudio(
        vagas
    )

valor_aluguel = imovel.calcular_aluguel()

while True:

    try:

        parcelas = ler_inteiro(
            "\nParcelamento do contrato (1 a 5): "
        )

        valor_parcela = (
            Contrato.calcular_parcelamento(parcelas)
        )

        break

    except ValueError as erro:

        print(erro)

print("\n" + "=" * 40)
print("ORÇAMENTO FINAL")
print("=" * 40)

print(
    f"Valor do aluguel: R$ {valor_aluguel:.2f}"
)

print(
    f"Valor do contrato: R$ 2000.00"
)

print(
    f"Parcelamento: {parcelas}x de R$ {valor_parcela:.2f}"
)

gerar = ler_sim_nao(
    "\nDeseja gerar o CSV? (S/N): "
)

if gerar:

    gerar_csv(valor_aluguel)