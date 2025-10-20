import tkinter as tk
from tkinter import ttk

class SelecaoProduto:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        
        # Frame principal
        main_frame = ttk.Frame(parent, padding="40")
        main_frame.pack(fill=tk.BOTH, expand=1)
        
        # Centralizar conteúdo
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Título
        titulo = ttk.Label(
            main_frame,
            text="Gerador de Código",
            font=('Arial', 20, 'bold')
        )
        titulo.grid(row=0, column=0, pady=(0, 10))
        
        # Subtítulo
        subtitulo = ttk.Label(
            main_frame,
            text="Selecione o tipo de produto",
            font=('Arial', 12),
            foreground='gray'
        )
        subtitulo.grid(row=1, column=0, pady=(0, 30))
        
        # Frame para a seleção
        frame_selecao = ttk.Frame(main_frame)
        frame_selecao.grid(row=2, column=0, pady=20)
        
        # Label do dropdown
        ttk.Label(
            frame_selecao,
            text="Tipo de Produto:",
            font=('Arial', 11, 'bold')
        ).pack(pady=(0, 10))
        
        # Produtos disponíveis
        self.produtos = {
            "Bastão Magnético": "bastao",
            "Grade Simples": "grade_simples",
            "Placa Magnética": "placa_magnetica",
            "Tampa Filtro": "tampa_filtro",
        }
        
        # Dropdown de produtos
        self.produto_var = tk.StringVar()
        self.combo_produtos = ttk.Combobox(
            frame_selecao,
            textvariable=self.produto_var,
            values=list(self.produtos.keys()),
            state='readonly',
            width=30,
            font=('Arial', 11)
        )
        self.combo_produtos.pack(pady=10)
        
        # Frame para os botões
        frame_botoes = ttk.Frame(main_frame)
        frame_botoes.grid(row=3, column=0, pady=40)
        
        # Botão OK
        btn_ok = ttk.Button(
            frame_botoes,
            text="OK",
            command=self.confirmar_produto,
            width=15
        )
        btn_ok.pack(side=tk.LEFT, padx=10)
        
        # Botão Cancelar
        btn_sair = ttk.Button(
            frame_botoes,
            text="Sair",
            command=self.app.root.quit,
            width=15
        )
        btn_sair.pack(side=tk.LEFT, padx=10)
    
    def confirmar_produto(self):
        """Confirma a seleção do produto"""
        produto_selecionado = self.produto_var.get()
        
        if not produto_selecionado:
            # Mostra mensagem de erro se nada foi selecionado
            return
        
        # Mapeia o produto para a função correspondente
        tipo_produto = self.produtos[produto_selecionado]
        
        if tipo_produto == "bastao":
            self.app.mostrar_formulario_bastao()
        elif tipo_produto == "grade_simples":
            self.app.mostrar_formulario_grade_simples()
        elif tipo_produto == "placa_magnetica":
            self.app.mostrar_formulario_placa_magnetica()
        elif tipo_produto == "tampa_filtro":
            self.app.mostrar_formulario_tampa_filtro()