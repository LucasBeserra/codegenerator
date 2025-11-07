class PlacaMagnetica(): 
    def __init__(self, tipo, dimensaoX, dimensaoY, altura, dimAbas, acabamento, especial):
        self.tipo = tipo
        self.dimensaoX = dimensaoX
        self.dimensaoY = dimensaoY
        self.altura = altura
        self.dimAbas = dimAbas
        self.acabamento = acabamento
        self.especial = especial

        MAP_TIPO = {
            "Placa com abas": "PA",
            "Placa com olhais": "PO"
        }

        MAP_DIMABAS = {
            "12": "A",
            "19": "B",
            "25": "C"
        }

        MAP_ACABAMENTO = {
            "Perolado": "J",
            "Polido": "P",
            "Escovado": "S"
        }
        
        MAP_ESPECIAL = {
            "Sim": "E",
            "Não": ""
        }

        self.codigo = (
            MAP_TIPO[tipo] +
            MAP_DIMABAS[dimAbas] +
            dimensaoX +
            dimensaoY +
            altura +
            MAP_ACABAMENTO[acabamento] +
            MAP_ESPECIAL[especial]
        )

    def __repr__(self):
        return self.codigo
