class GradeSimples(): 
    def __init__(self, fechamento, acabamento, perfil, fita, comprimento, altura, especial):
        self.fechamento = fechamento
        self.acabamento = acabamento
        self.perfil = perfil
        self.comprimento = comprimento
        self.altura = altura
        self.especial = especial


        MAP_FECHAMENTO = {
            "Tipo A": "A",
            "Tipo B": "B",
            "Tipo C": "C",
        }

        MAP_ACABAMENTO = {
            "Amarelo": "J",
            "Azul": "P",
            "Vermelho": "E"
        }

        MAP_PERFIL = {
            "Quadrada": "Q",
            "Redonda": "R",
            "Trapezoidal": "T"
        }

        MAP_FITA = {
            "2MM": "A",
            "3MM": "B",
            "4,76MM": "C",
        }

        MAP_ESPECIAL = {
            "Sim": "E",
            "Não": ""
        }

        self.codigo = (
            "G" +
            MAP_FECHAMENTO[fechamento] +
            MAP_ACABAMENTO[acabamento] +
            MAP_PERFIL[perfil] +
            MAP_FITA[fita] +
            comprimento +
            altura +
            MAP_ESPECIAL[especial]
        )

    def testeInicial(self):
        print("Hello, sou uma grade magnética simples")

