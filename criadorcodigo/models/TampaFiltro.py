class TampaFiltro():
    def __init__(self, fechamento, acabamento, perfil, comprimento, altura, especial):
        self.fechamento = fechamento
        self.acabamento = acabamento
        self.perfil = perfil
        self.comprimento = comprimento
        self.altura = altura
        self.especial = especial
        
        MAP_FECHAMENTO = {
            "Hermético": "H",
            "Recravado": "R",
        }
        
        MAP_ACABAMENTO = {
            "Jateado": "J",
            "Polido": "P",
            "Escovado": "S"
        }
        
        MAP_ESPECIAL = {
            "Sim": "E",
            "Não": ""
        }

        self.codigo = (
            MAP_FECHAMENTO[fechamento] +
            MAP_ACABAMENTO[acabamento] +
            MAP_ESPECIAL[especial]
        )

    def testeInicial(self):
        print("Hello, sou uma tampa filtro")

    def __repr__(self):
        return self.codigo

    def __repr__(self):
        return self.codigo