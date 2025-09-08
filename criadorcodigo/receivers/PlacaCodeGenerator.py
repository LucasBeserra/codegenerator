from models.Placa import PlacaMagnetica
import questionary

def criar_placa():
    parametros = []

    parametros.append(
        questionary.select("Tipo:", choices=["Placa com abas", "Placa com olhais"]).ask()
    )
    
    parametros.append(
        input("Dimensão X (mm): ")
    )
    
    parametros.append(
        input("Dimensão Y (mm): ")
    )
    
    parametros.append(
        input("Altura (mm): ")
    )
    
    parametros.append(
        questionary.select("Dimensão das abas:", choices=["12", "19", "25"]).ask()
    )

    parametros.append(
        questionary.select("Acabamento:", choices=["Jateado", "Polido", "Escovado"]).ask()
    )

    parametros.append(
        questionary.select("É especial?", choices=["Sim", "Não"]).ask()
    )

    def createPlaca(parametros):
        return PlacaMagnetica(*parametros)

    placa = createPlaca(parametros)

    print("\n Código criado com sucesso: " + placa.codigo)
    input("\nPressione Enter para voltar ao menu...")
    
    
    