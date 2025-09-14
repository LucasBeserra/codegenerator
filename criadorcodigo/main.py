import questionary

from receivers.BastaoCodeGenerator import form_bastao
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

        if escolha == produtos[0]:
            form_bastao()

        elif escolha == produtos[1]:
            criar_tampa()

        elif escolha == produtos[2]:
            criar_grade()

        elif escolha == produtos[3]:
            criar_placa()

        elif escolha == produtos[4]:
            print("Encerrando o programa...")
            break  # Sai do loop e encerra o programa

if __name__ == "__main__":
    main()
