class GradeSimples(): 
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
            "Escovado": "E"
        }

        MAP_PERFIL = {
            "Quadrada": "Q",
            "Redonda": "R",
            "Trapezoidal": "T"
        }

        MAP_ESPECIAL = {
            "Sim": "E",
            "Não": ""
        }

        self.codigo = (
            MAP_FECHAMENTO[fechamento] +
            MAP_ACABAMENTO[acabamento] +
            MAP_ESPECIAL[especial] +
            MAP_PERFIL[perfil]
        )

    def testeInicial(self):
        print("Hello, sou uma grade magnética simples")

