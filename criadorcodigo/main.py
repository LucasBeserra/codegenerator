import tkinter as tk
from tkinter import ttk
import sys
import os

# Adiciona a pasta pai ao path
pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, pasta_raiz)

class AplicacaoPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Código")
        self.root.geometry("800x700")
        self.root.resizable(False, False)
        
        self.frame_atual = None
        self.mostrar_selecao_produto()
    
    def limpar_janela(self):
        """Remove o frame atual"""
        if self.frame_atual:
            self.frame_atual.destroy()
            self.frame_atual = None
    
    def mostrar_selecao_produto(self):
        """Exibe a página de seleção de produto"""
        self.limpar_janela()
        
        # Importa a classe de seleção
        from interface.views.SelecaoProduto import SelecaoProduto
        
        self.frame_atual = ttk.Frame(self.root)
        self.frame_atual.pack(fill=tk.BOTH, expand=1)
        
        # Passa referência ao aplicativo para navegação
        selecao = SelecaoProduto(self.frame_atual, self)
    
    def mostrar_formulario_bastao(self):
        """Exibe o formulário do bastão"""
        self.limpar_janela()
        
        # Importa a classe do formulário bastão
        from interface.views.FormBastao import FormularioBastao
        
        self.frame_atual = ttk.Frame(self.root)
        self.frame_atual.pack(fill=tk.BOTH, expand=1)
        
        # Passa referência ao aplicativo para voltar
        formulario = FormularioBastao(self.frame_atual, self)
    
    def mostrar_formulario_grade_simples(self):
        """Exibe o formulário da grade simples"""
        self.limpar_janela()
        
        # Importa a classe do formulário grade simples
        from interface.views.FormGradeSimples import FormularioGradeSimples
        
        self.frame_atual = ttk.Frame(self.root)
        self.frame_atual.pack(fill=tk.BOTH, expand=1)
        
        # Passa referência ao aplicativo para voltar
        formulario = FormularioGradeSimples(self.frame_atual, self)
    
    def mostrar_formulario_placa_magnetica(self):
        """Exibe o formulário da placa magnética"""
        self.limpar_janela()
        
        # Importa a classe do formulário placa magnética
        from interface.views.FormPlaca import FormularioPlacaMagnetica
        
        self.frame_atual = ttk.Frame(self.root)
        self.frame_atual.pack(fill=tk.BOTH, expand=1)
        
        # Passa referência ao aplicativo para voltar
        formulario = FormularioPlacaMagnetica(self.frame_atual, self)
    
    def mostrar_formulario_tampa_filtro(self):
        """Exibe o formulário da tampa filtro"""
        self.limpar_janela()
        
        # Importa a classe do formulário tampa filtro
        from interface.views.FormTampaFiltro import FormularioTampaFiltro
        
        self.frame_atual = ttk.Frame(self.root)
        self.frame_atual.pack(fill=tk.BOTH, expand=1)
        
        # Passa referência ao aplicativo para voltar
        formulario = FormularioTampaFiltro(self.frame_atual, self)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoPrincipal(root)
    root.mainloop()