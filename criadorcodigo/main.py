import questionary

from receivers.BastaoCodeGenerator import criar_bastao
from receivers.GradeCodeGenerator import criar_grade
from receivers.PlacaCodeGenerator import criar_placa
from receivers.TampaCodeGenerator import criar_tampa


def main():

    produtos = [
            "Bastao",
            "Filtro",
            "Grade",
            "Placa",
            "Sair"
            ]
    
    while True:
        escolha = questionary.select(
            "O que deseja criar?",
            choices=[*produtos]
        ).ask()

        if escolha == "Bastao":
            criar_bastao()

        elif escolha == "Tampa Filtro":
            criar_tampa()

        elif escolha == "Grade simples":
            criar_grade()

        elif escolha == "Placa magnética":
            criar_placa()

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