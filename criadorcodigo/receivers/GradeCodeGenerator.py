from models.GradeSimples import GradeSimples
import questionary

def criar_grade():
    parametros = []

    parametros.append(
        questionary.select("Fechamento:", choices=["Hermético", "Recravado"]).ask()
    )
    
    parametros.append(
        questionary.select("Acabamento:", choices=["Jateado", "Polido", "Escovado"]).ask()
    )
    
    parametros.append(
        questionary.select("Perfil:", choices=["Quadrada", "Redonda", "Trapezoidal"]).ask()
    )
    
    parametros.append(
        input("Comprimento (mm): ")
    )
    
    parametros.append(
        input("Altura (mm): ")
    )
    
    parametros.append(
        questionary.select("É especial?", choices=["Sim", "Não"]).ask()
    )
    
    def createGrade(parametros):
        return GradeSimples(*parametros)

    grade = createGrade(parametros)

    print("\n Código criado com sucesso: " + grade.codigo)
    input("\nPressione Enter para voltar ao menu...")
    