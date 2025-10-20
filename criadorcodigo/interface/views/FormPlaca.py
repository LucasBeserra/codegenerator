import tkinter as tk
from tkinter import ttk

class FormularioPlacaMagnetica:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        
        # Frame principal com scroll
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=1)
        
        # Canvas para scroll
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Frame dentro do canvas
        frame = ttk.Frame(canvas, padding="20")
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        # Título
        ttk.Label(frame, text="Gerador de Código - Placa Magnética", 
                  font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        row = 1
        
        # 1. Tipo
        ttk.Label(frame, text="Tipo:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.tipo_var = tk.StringVar()
        tipo_combo = ttk.Combobox(frame, textvariable=self.tipo_var, 
                                  values=["Placa com abas", "Placa com olhais"], 
                                  state='readonly', width=47)
        tipo_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 2. Dimensão X
        ttk.Label(frame, text="Dimensão X:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.dimensao_x_entry = ttk.Entry(frame, width=50)
        self.dimensao_x_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 100, 150, 200)", font=('Arial', 8), 
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
        # 3. Dimensão Y
        ttk.Label(frame, text="Dimensão Y:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.dimensao_y_entry = ttk.Entry(frame, width=50)
        self.dimensao_y_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 100, 150, 200)", font=('Arial', 8),
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
        # 4. Altura
        ttk.Label(frame, text="Altura:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.altura_entry = ttk.Entry(frame, width=50)
        self.altura_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 10, 20, 30)", font=('Arial', 8),
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
        # 5. Dimensão Abas
        ttk.Label(frame, text="Dimensão Abas:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.dim_abas_var = tk.StringVar()
        dim_abas_combo = ttk.Combobox(frame, textvariable=self.dim_abas_var,
                                      values=["12", "19", "25"],
                                      state='readonly', width=47)
        dim_abas_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 6. Acabamento
        ttk.Label(frame, text="Acabamento:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.acabamento_var = tk.StringVar()
        acabamento_combo = ttk.Combobox(frame, textvariable=self.acabamento_var,
                                        values=["Perolado", "Polido", "Escovado"],
                                        state='readonly', width=47)
        acabamento_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 7. Especial
        ttk.Label(frame, text="Especial:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.especial_var = tk.StringVar()
        especial_combo = ttk.Combobox(frame, textvariable=self.especial_var,
                                      values=["Sim", "Não"],
                                      state='readonly', width=47)
        especial_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # Frame para os botões
        frame_botoes = ttk.Frame(frame)
        frame_botoes.grid(row=row, column=0, columnspan=2, pady=30)
        
        # Botão Voltar
        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=self.voltar)
        btn_voltar.pack(side=tk.LEFT, padx=5)
        
        # Botão Gerar
        btn_gerar = ttk.Button(frame_botoes, text="Gerar Código", command=self.gerar_codigo)
        btn_gerar.pack(side=tk.LEFT, padx=5)
        
        row += 1
        
        # Separador
        ttk.Separator(frame, orient='horizontal').grid(row=row, column=0, columnspan=2, 
                                                       sticky='ew', pady=10)
        row += 1
        
        # Label para o código gerado
        ttk.Label(frame, text="Código Gerado:", font=('Arial', 12, 'bold')).grid(
            row=row, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        row += 1
        
        # Campo de texto não editável para mostrar o código
        self.codigo_text = tk.Text(
            frame, 
            width=70, 
            height=3,
            state='disabled',
            font=('Courier New', 14, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50',
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.codigo_text.grid(row=row, column=0, columnspan=2, pady=5)
    
    def voltar(self):
        """Volta para a página de seleção de produto"""
        self.app.mostrar_selecao_produto()
    
    def gerar_codigo(self):
        """Função chamada quando o botão é clicado"""
        # Pega os valores dos campos
        tipo = self.tipo_var.get()
        dimensao_x = self.dimensao_x_entry.get().strip()
        dimensao_y = self.dimensao_y_entry.get().strip()
        altura = self.altura_entry.get().strip()
        dim_abas = self.dim_abas_var.get()
        acabamento = self.acabamento_var.get()
        especial = self.especial_var.get()
        
        # Validação básica
        campos_vazios = []
        if not tipo:
            campos_vazios.append("Tipo")
        if not dimensao_x:
            campos_vazios.append("Dimensão X")
        if not dimensao_y:
            campos_vazios.append("Dimensão Y")
        if not altura:
            campos_vazios.append("Altura")
        if not dim_abas:
            campos_vazios.append("Dimensão Abas")
        if not acabamento:
            campos_vazios.append("Acabamento")
        if not especial:
            campos_vazios.append("Especial")
        
        if campos_vazios:
            mensagem = "⚠️ Preencha os seguintes campos:\n" + "\n".join(f"• {campo}" for campo in campos_vazios)
            self.mostrar_codigo(mensagem)
            return
        
        try:
            # Importa e instancia o modelo PlacaMagnetica
            from models.Placa import PlacaMagnetica
            
            # Cria o objeto com os dados do formulário
            placa = PlacaMagnetica(
                tipo=tipo,
                dimensaoX=dimensao_x,
                dimensaoY=dimensao_y,
                altura=altura,
                dimAbas=dim_abas,
                acabamento=acabamento,
                especial=especial
            )
            
            # Pega o código gerado
            codigo_gerado = str(placa)
            
            # Mostra o código no campo
            self.mostrar_codigo(f"✓ Código gerado com sucesso!\n\n{codigo_gerado}")
            
        except KeyError as e:
            self.mostrar_codigo(f"❌ ERRO: Valor inválido selecionado: {str(e)}")
        except Exception as e:
            self.mostrar_codigo(f"❌ ERRO ao gerar código:\n{str(e)}")
    
    def mostrar_codigo(self, texto):
        """Atualiza o campo de código com o texto gerado"""
        # Habilita temporariamente para editar
        self.codigo_text.config(state='normal')
        
        # Limpa o conteúdo anterior
        self.codigo_text.delete('1.0', tk.END)
        
        # Insere o novo código
        self.codigo_text.insert('1.0', texto)
        
        # Desabilita novamente (não editável)
        self.codigo_text.config(state='disabled')