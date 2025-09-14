from models.Bastao import Bastao
import questionary

def form_bastao():
    
    parametros = []

    parametros.append(
        questionary.select("Fechamento:", choices=["Tipo A", "Tipo B", "Tipo C"]).ask()
    )
    parametros.append(
        questionary.select("Acabamento:", choices=["Amarelo", "Azul", "Vermelho"]).ask()
    )
    parametros.append(
        questionary.select("Diâmetro (mm):", choices=["19", "25", "12"]).ask()
    )
    parametros.append(
        input("Comprimento (mm): ")
    )
    parametros.append(
        questionary.select("Rosca:", choices=["M4", "M6", "M8", "M10", "Sem Rosca"]).ask()
    )
    
    if parametros[4] == "Sem Rosca":
        parametros.append("Não se aplica"),
        parametros.append(""),
    else:
        parametros.append(
            questionary.select("Tipo de Rosca:", choices=["Interno", "Externo"]).ask()
        )

        parametros.append(
            input("Comprimento da rosca (mm): ")
        )

    parametros.append(
        questionary.select("Acoplamento:", choices=["Tipo A", "Tipo B"]).ask()
    )
    parametros.append(
        questionary.select("É especial?", choices=["Sim", "Não"]).ask()
    )

    def criarCodigo(parametros):
        return Bastao(*parametros)

    bastao = criarCodigo(parametros)
    
    print("\n Código criado com sucesso: " + bastao.codigo)
    input("\nPressione Enter para voltar ao menu...")



