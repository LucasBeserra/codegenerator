import tkinter as tk
import sys
import os

# Adiciona a pasta pai ao path
pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, pasta_raiz)

from Aplicacao import Aplicacao

def main():
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()

if __name__ == "__main__":
    main()