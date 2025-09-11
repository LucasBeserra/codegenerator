# import questionary

class BastaoMagnetico(): 
    def __init__(self, fechamento, acabamento, diametro, comprimento,
                 rosca, tipo_rosca, comprimento_rosca, acoplamento, especial):
        self.fechamento = fechamento
        self.acabamento = acabamento
        self.diametro = diametro
        self.comprimento = comprimento
        self.rosca = rosca
        self.tipo_rosca = tipo_rosca
        self.comprimento_rosca = comprimento_rosca
        self.acoplamento = acoplamento
        self.especial = especial

        # Mapas de código por campo
        MAP_FECHAMENTO = {
            "Amarelo": "A",
            "Vermelho": "V",
        }

        MAP_ACABAMENTO = {
            "Verde prateado": "J",
            "Cinza médio": "P",
            "Perolado": "S"
        }

        MAP_ROSCA = {
            "Métrica": "A",
            "Unificada": "B",
            "Fina": "C",
            "Extra fina": "D"
        }

        MAP_TIPO_ROSCA = {
            "Interno": "I",
            "Externo": "E",
            "Não se aplica": "N"
        }

        MAP_ACOPLAMENTO = {
            "Marrom": "MR",
            "Laranja Esférico": "LE"
        }

        MAP_ESPECIAL = {
            "Sim": "E",
            "Não": ""
        }
    
        self.codigo = (
        MAP_FECHAMENTO[fechamento] +
        MAP_ACABAMENTO[acabamento] +
        diametro +
        comprimento +
        MAP_ROSCA[rosca] +
        MAP_TIPO_ROSCA[tipo_rosca] +
        comprimento_rosca +
        MAP_ACOPLAMENTO[acoplamento] +
        MAP_ESPECIAL[especial]
        )

    def testeInicial(self):
        print("Hello, sou um bastão magnético")


    def __repr__(self):
        return self.codigo
    

    # def inputsReceiver(self): 
    #     parametros = []

    #     parametros.append(questionary.select("Fechamento:", choices=["Hermético", "Recravado"]).ask())
    #     parametros.append(questionary.select("Acabamento:", choices=["Jateado", "Polido", "Escovado"]).ask())
    #     parametros.append(questionary.select("Diâmetro (mm):", choices=["19", "25", "12"]).ask())
    #     parametros.append(input("Comprimento (mm): "))
    #     parametros.append(questionary.select("Rosca:", choices=["M4", "M6", "M8", "Sem Rosca"]).ask())
    #     parametros.append(questionary.select("Tipo de Rosca:", choices=["Interno", "Externo", "Não se aplica"]).ask())
    #     parametros.append(input("Comprimento da rosca (mm): "))
    #     parametros.append(questionary.select("É especial?", choices=["Sim", "Não"]).ask())
    #     parametros.append(questionary.select("Acoplamento:", choices=["Filtro Magnético", "Tampa filtro"]).ask())
        
    #     def createBastao(parametros):
    #         return BastaoMagnetico(*parametros)

    #     bastao = createBastao(parametros)

    #     print("\n Código criado com sucesso:")
    #     print(bastao)


# bastao = BastaoMagnetico("Bastão")
# bastao.testeInicial()