# import questionary

class Bastao(): 
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
            "Tipo A": "A",
            "Tipo B": "B",
            "Tipo C": "C",
        }

        MAP_ACABAMENTO = {
            "Amarelo": "AM",
            "Azul": "AZ",
            "Vermelho": "VM",
        }

        MAP_ROSCA = {
            "M4": "A",
            "M6": "B",
            "M8": "C",
            "M10": "D",
            "Sem Rosca": "N"
        }

        MAP_TIPO_ROSCA = {
            "Interno": "I",
            "Externo": "E",
            "Não se aplica": "N"
        }

        MAP_ACOPLAMENTO = {
            "Tipo A": "TA",
            "Tipo B": "TB",
            "Não se aplica": ""
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
    