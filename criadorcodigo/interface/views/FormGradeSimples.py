import tkinter as tk
from tkinter import ttk

class FormularioGradeSimples:
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
        ttk.Label(frame, text="Gerador de Código - Grade Simples", 
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
        
        # 3. Perfil
        ttk.Label(frame, text="Perfil:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.perfil_var = tk.StringVar()
        perfil_combo = ttk.Combobox(frame, textvariable=self.perfil_var,
                                    values=["Quadrada", "Redonda", "Trapezoidal"],
                                    state='readonly', width=47)
        perfil_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1

        # 4. Fita
        ttk.Label(frame, text="Fita:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.fita_var = tk.StringVar()
        perfil_combo = ttk.Combobox(frame, textvariable=self.fita_var,
                                    values=["2MM", "3MM", "4,76MM", "6,35MM"],
                                    state='readonly', width=47)
        perfil_combo.grid(row=row, column=1, pady=5, padx=5)
        row += 1
        
        # 4. Comprimento / Diâmetro
        ttk.Label(frame, text="Comprimento/Diâmetro:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.comprimento_entry = ttk.Entry(frame, width=50)
        self.comprimento_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 100, 200, 300)", font=('Arial', 8), 
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2

        # 5. Largura
        ttk.Label(frame, text="Largura:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.largura_entry = ttk.Entry(frame, width=50)
        self.largura_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(obs: Se o perfil for redondo, deixe em branco)", font=('Arial', 8), 
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
        # 6. Altura
        ttk.Label(frame, text="Altura:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.altura_entry = ttk.Entry(frame, width=50)
        self.altura_entry.grid(row=row, column=1, pady=5, padx=5)
        ttk.Label(frame, text="(ex: 50, 75, 100)", font=('Arial', 8),
                  foreground='gray').grid(row=row+1, column=1, sticky=tk.W, padx=5)
        row += 2
        
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
        perfil = self.perfil_var.get()
        fita = self.fita_var.get()
        comprimento = self.comprimento_entry.get().strip()
        largura = self.largura_entry.get().strip()
        altura = self.altura_entry.get().strip()
        especial = self.especial_var.get()
        
        # Validação básica
        campos_vazios = []
        if not fechamento:
            campos_vazios.append("Fechamento")
        if not acabamento:
            campos_vazios.append("Acabamento")
        if not perfil:
            campos_vazios.append("Perfil")
        if not comprimento:
            campos_vazios.append("Comprimento")
        if not altura:
            campos_vazios.append("Altura")
        if not especial:
            campos_vazios.append("Especial")
        
        if campos_vazios:
            mensagem = "⚠️ Preencha os seguintes campos:\n" + "\n".join(f"• {campo}" for campo in campos_vazios)
            self.mostrar_codigo(mensagem)
            return
        
        try:
            # Importa e instancia o modelo GradeSimples
            from models.GradeSimples import GradeSimples
            
            # Cria o objeto com os dados do formulário
            grade = GradeSimples(
                fechamento=fechamento,
                acabamento=acabamento,
                perfil=perfil,
                fita=fita,
                comprimento=comprimento,
                largura=largura,
                altura=altura,
                especial=especial
            )
            
            # Pega o código gerado
            codigo_gerado = grade.codigo
            
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