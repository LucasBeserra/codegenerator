import tkinter as tk
from tkinter import ttk

class FormularioBastao:
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
        ttk.Label(frame, text="Gerador de Código - Bastão Magnético", 
                  font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        row = 1
        
        # 1. Fechamento
        ttk.Label(frame, text="Fechamento:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.fechamento_var = tk.StringVar()
        fechamento_combo = ttk.Combobox(frame, textvariable=self.fechamento_var, 
                                        values=["Tipo A", "Tipo B", "Tipo C"], 
                                        state='readonly', width=47)
        fechamento_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 2. Acabamento
        ttk.Label(frame, text="Acabamento:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.acabamento_var = tk.StringVar()
        acabamento_combo = ttk.Combobox(frame, textvariable=self.acabamento_var,
                                        values=["Amarelo", "Azul", "Vermelho"],
                                        state='readonly', width=47)
        acabamento_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 3. Diâmetro
        ttk.Label(frame, text="Diâmetro:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.diametro_entry = ttk.Entry(frame, width=50)
        self.diametro_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 12.7, 19,05, 25,4)", font=('Arial', 8),
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
        # 4. Comprimento
        ttk.Label(frame, text="Comprimento:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.comprimento_entry = ttk.Entry(frame, width=50)
        self.comprimento_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 100, 200, 300)", font=('Arial', 8),
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
        # 5. Rosca
        ttk.Label(frame, text="Rosca:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.rosca_var = tk.StringVar()
        rosca_combo = ttk.Combobox(frame, textvariable=self.rosca_var,
                                   values=["M4", "M6", "M8", "M10", "Sem Rosca"],
                                   state='readonly', width=47)
        rosca_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 6. Tipo de Rosca
        ttk.Label(frame, text="Tipo de Rosca:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.tipo_rosca_var = tk.StringVar()
        tipo_rosca_combo = ttk.Combobox(frame, textvariable=self.tipo_rosca_var,
                                        values=["Interno", "Externo", "Não se aplica"],
                                        state='readonly', width=47)
        tipo_rosca_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 7. Comprimento da Rosca
        ttk.Label(frame, text="Comprimento Rosca:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.comprimento_rosca_entry = ttk.Entry(frame, width=50)
        self.comprimento_rosca_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 8, 10, 12 ou deixe vazio se não aplicável)", 
                  font=('Arial', 8), foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
        # 8. Acoplamento
        ttk.Label(frame, text="Acoplamento:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.acoplamento_var = tk.StringVar()
        acoplamento_combo = ttk.Combobox(frame, textvariable=self.acoplamento_var,
                                         values=["Tipo A", "Tipo B", "Não se aplica"],
                                         state='readonly', width=47)
        acoplamento_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 9. Especial
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
        
        # Botão Gerar
        btn_gerar = ttk.Button(frame_botoes, text="Gerar Código", command=self.gerar_codigo)
        btn_gerar.pack(side=tk.LEFT, padx=5)

        # Botão Voltar
        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=self.voltar)
        btn_voltar.pack(side=tk.LEFT, padx=5)
        
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
        fechamento = self.fechamento_var.get()
        acabamento = self.acabamento_var.get()
        diametro = self.diametro_entry.get().strip()
        comprimento = self.comprimento_entry.get().strip()
        rosca = self.rosca_var.get()
        tipo_rosca = self.tipo_rosca_var.get()
        comprimento_rosca = self.comprimento_rosca_entry.get().strip()
        acoplamento = self.acoplamento_var.get()
        especial = self.especial_var.get()
        
        # Validação básica
        campos_vazios = []
        if not fechamento:
            campos_vazios.append("Fechamento")
        if not acabamento:
            campos_vazios.append("Acabamento")
        if not diametro:
            campos_vazios.append("Diâmetro")
        if not comprimento:
            campos_vazios.append("Comprimento")
        if not rosca:
            campos_vazios.append("Rosca")
        if not tipo_rosca:
            campos_vazios.append("Tipo de Rosca")
        if not comprimento_rosca:
            campos_vazios.append("Comprimento Rosca")
        if not acoplamento:
            campos_vazios.append("Acoplamento")
        if not especial:
            campos_vazios.append("Especial")
        
        if campos_vazios:
            mensagem = "⚠️ Preencha os seguintes campos:\n" + "\n".join(f"• {campo}" for campo in campos_vazios)
            self.mostrar_codigo(mensagem)
            return
        
        try:
            # Importa e instancia o modelo Bastao
            from models.Bastao import Bastao
            
            # Cria o objeto com os dados do formulário
            bastao = Bastao(
                fechamento=fechamento,
                acabamento=acabamento,
                diametro=diametro,
                comprimento=comprimento,
                rosca=rosca,
                tipo_rosca=tipo_rosca,
                comprimento_rosca=comprimento_rosca,
                acoplamento=acoplamento,
                especial=especial
            )
            
            # Pega o código gerado (usa __repr__)
            codigo_gerado = str(bastao)
            
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