import questionary

from models.BastaoMagnetico import BastaoMagnetico
from receivers.BastaoGeneratorCode import criar_bastao
# from GradeSimples import GradeSimples
# from Placa import PlacaMagnetica
# from TampaFiltro import TampaFiltro


def main():

    produtos = [
            "Bastao",
            "Tampa Filtro",
            "Grade simples",
            "Placa magnética",
            "Sair"
            ]
    
    while True:
        escolha = questionary.select(
            "O que deseja criar?",
            choices=[*produtos]
        ).ask()

        if escolha == "Bastao":
            criar_bastao()

        elif escolha == "Sair":
            print("Encerrando o programa...")
            break  # Sai do loop e encerra o programa

if __name__ == "__main__":
    main()




# elif categoria == "Tampa Filtro":
#     tampaFiltro = TampaFiltro("Tampa de filtro")
#     tampaFiltro.testeInicial()

# elif categoria == "Grade simples":
#     gradeSimples = GradeSimples("Grade simples")
#     gradeSimples.testeInicial()

# elif categoria == "Placa magnética":
#     placaMag = PlacaMagnetica("Placa magnética")
#     placaMag.testeInicial()