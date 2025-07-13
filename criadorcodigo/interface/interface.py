import tkinter as tk
from tkinter import ttk

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Generator")
        self.geometry("500x800")

        self.label = ttk.Label(self, text="Olá, mundo!")
        self.label.pack(pady=10)

        self.botao = ttk.Button(self, text="Clique aqui", command=self.acao_botao)
        self.botao.pack(pady=10)

    def acao_botao(self):
        self.label.config(text="Botão clicado!")
