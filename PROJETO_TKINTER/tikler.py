import tkinter as tk 
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import json
import os
import webbrowser
import unicodedata

# ===================== ARQUIVO JSON (USUÁRIOS) =====================
USERS_FILE = "usuarios.json"

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({"admin": "1234"}, f, indent=4)

def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ===================== ARQUIVO JSON (ALUNOS) =====================
ARQUIVO_ALUNOS = "alunos.json"

def carregar_alunos():
    if not os.path.exists(ARQUIVO_ALUNOS):
        with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_alunos(alunos):
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=4)

# ===================== ARQUIVO JSON (DISCIPLINAS) =====================
ARQUIVO_DISCIPLINAS = "disciplinas.json"

def carregar_disciplinas():
    if not os.path.exists(ARQUIVO_DISCIPLINAS):
        with open(ARQUIVO_DISCIPLINAS, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
    with open(ARQUIVO_DISCIPLINAS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_disciplinas(disciplinas):
    with open(ARQUIVO_DISCIPLINAS, "w", encoding="utf-8") as f:
        json.dump(disciplinas, f, ensure_ascii=False, indent=4)

# ===================== ARQUIVO JSON (NOTAS) =====================
ARQUIVO_NOTAS = "notas.json"

def carregar_notas():
    if not os.path.exists(ARQUIVO_NOTAS):
        with open(ARQUIVO_NOTAS, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
    with open(ARQUIVO_NOTAS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_notas(notas):
    with open(ARQUIVO_NOTAS, "w", encoding="utf-8") as f:
        json.dump(notas, f, ensure_ascii=False, indent=4)

# ===================== ARQUIVO JSON (FALTAS) =====================
ARQUIVO_FALTAS = "faltas.json"

def carregar_faltas():
    if not os.path.exists(ARQUIVO_FALTAS):
        with open(ARQUIVO_FALTAS, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
    with open(ARQUIVO_FALTAS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_faltas(faltas):
    with open(ARQUIVO_FALTAS, "w", encoding="utf-8") as f:
        json.dump(faltas, f, ensure_ascii=False, indent=4)

# ===================== INICIALIZAÇÃO DO SISTEMA =====================
def inicializar_sistema():
    """Garante que os dados iniciais estejam no sistema"""
    alunos = carregar_alunos()
    disciplinas = carregar_disciplinas()
    
    # Adicionar aluno exemplo se não existir
    aluno_encontrado = any(aluno.get("RA") == "H764113" for aluno in alunos)
    if not aluno_encontrado:
        alunos.append({
            "nome": "Bruno Augusto Gimenez Alves",
            "RA": "H764113",
            "turma": "ADS2",
            "curso": "ADS",
            "email": "H764113"
        })
        salvar_alunos(alunos)
    
    # Adicionar disciplinas exemplo se não existirem
    disciplinas_exemplo = [
        {"nome": "Engenharia de Software", "codigo": "ENG001", "professor": "Raul", "carga_horaria": "80"},
        {"nome": "Programação Python", "codigo": "PYT002", "professor": "Aldy", "carga_horaria": "60"},
        {"nome": "Programação C++", "codigo": "CPP003", "professor": "Roger", "carga_horaria": "70"}
    ]
    
    for disc in disciplinas_exemplo:
        if not any(d.get("codigo") == disc["codigo"] for d in disciplinas):
            disciplinas.append(disc)
    
    salvar_disciplinas(disciplinas)

# ===================== FUNÇÃO PADRÃO PARA LISTAGEM COM TABELA =====================
def criar_janela_listagem(titulo, dados, colunas, largura_colunas=None, parent_window=None):
    """Função padrão para criar janelas de listagem com tabela"""
    lista_janela = tk.Toplevel()
    lista_janela.title(titulo)
    lista_janela.geometry("800x550")
    lista_janela.configure(bg="#d9d9d9")

    # Frame do título
    titulo_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    titulo_frame.pack(fill="x", pady=10)
    
    tk.Label(titulo_frame, text=titulo, bg="#d9d9d9",
             font=("Arial", 14, "bold")).pack()

    # Frame da tabela
    frame_tabela = tk.Frame(lista_janela, bg="#d9d9d9")
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    if not dados:
        tk.Label(frame_tabela, text=f"Nenhum registro cadastrado.",
                 bg="#d9d9d9", font=("Arial", 11)).pack()
    else:
        # Criar Treeview com estilo melhorado
        style = ttk.Style()
        style.configure("Treeview", 
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        style.configure("Treeview.Heading",
                        background="#4CAF50",
                        foreground="white",
                        font=("Arial", 10, "bold"))
        style.map("Treeview", 
          background=[("selected", "#4CAF50")],
          foreground=[("selected", "black")])


        tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=15)
        
        # Definir headings
        for col in colunas:
            tree.heading(col, text=col)
        
        # Definir larguras das colunas
        for i, col in enumerate(colunas):
            if largura_colunas and i < len(largura_colunas):
                tree.column(col, width=largura_colunas[i], anchor="center")
            else:
                tree.column(col, width=120, anchor="center")
        
        # Adicionar scrollbars
        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Inserir dados - CORREÇÃO AQUI
        for item in dados:
            # Para cada item, criar uma lista de valores na ordem das colunas
            valores = []
            for col in colunas:
                # Converter o nome da coluna para chave do dicionário (minúsculo, sem espaços)
                chave = col.lower().replace(" ", "_")
                valor = item.get(chave, '-')
                valores.append(valor)
            tree.insert("", "end", values=valores)
        
        # Posicionar elementos
        tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Configurar grid weights
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

    # Frame dos botões
    btn_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    btn_frame.pack(pady=10)

    # Função para voltar ao menu
    def voltar_menu():
        lista_janela.destroy()
        if parent_window:
            parent_window.deiconify()

    # Botão Voltar ao Menu
    btn_voltar_menu = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=voltar_menu)
    btn_voltar_menu.pack(side="left", padx=5)

    # Botão Adicionar (se aplicável)
    if titulo == "Alunos Cadastrados":
        btn_adicionar = tk.Button(btn_frame, text="Adicionar Novo Aluno", bg="#4CAF50", fg="white",
                                font=("Arial", 10, "bold"), relief="raised", 
                                command=lambda: [lista_janela.destroy(), abrir_tela_cadastro(parent_window)])
        btn_adicionar.pack(side="left", padx=5)
    elif titulo == "Disciplinas Cadastradas":
        btn_adicionar = tk.Button(btn_frame, text="Adicionar Nova Disciplina", bg="#4CAF50", fg="white",
                                font=("Arial", 10, "bold"), relief="raised", 
                                command=lambda: [lista_janela.destroy(), abrir_tela_disciplinas(parent_window)])
        btn_adicionar.pack(side="left", padx=5)
    elif titulo == "Notas Cadastradas":
        btn_adicionar = tk.Button(btn_frame, text="Adicionar Nova Nota", bg="#4CAF50", fg="white",
                                font=("Arial", 10, "bold"), relief="raised", 
                                command=lambda: [lista_janela.destroy(), abrir_tela_notas(parent_window)])
        btn_adicionar.pack(side="left", padx=5)
    elif titulo == "Faltas Cadastradas":
        btn_adicionar = tk.Button(btn_frame, text="Adicionar Nova Falta", bg="#4CAF50", fg="white",
                                font=("Arial", 10, "bold"), relief="raised", 
                                command=lambda: [lista_janela.destroy(), abrir_tela_faltas(parent_window)])
        btn_adicionar.pack(side="left", padx=5)
    
    return lista_janela

# ===================== TELA DE ALUNOS =====================
def listar_alunos(parent_window=None):
    if parent_window:
        parent_window.withdraw()
    
    alunos = carregar_alunos()
    dados_formatados = []
    for aluno in alunos:
        dados_formatados.append({
            "nome": aluno.get('nome', '-'),
            "ra": aluno.get('RA', '-'),
            "turma": aluno.get('turma', '-'),
            "curso": aluno.get('curso', '-')
        })
    
    criar_janela_listagem(
        "Alunos Cadastrados",
        dados_formatados,
        ["Nome", "RA", "Turma", "Curso"],
        [300, 120, 100, 150],
        parent_window
    )

def abrir_tela_cadastro(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Aluno")
    janela_cadastro.geometry("500x450")
    janela_cadastro.config(bg="#dcdcdc")

    # Frame principal
    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título
    tk.Label(main_frame, text="Cadastro de Aluno", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Nome:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
    nome_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    nome_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="RA:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
    ra_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    ra_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Turma:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
    turma_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    turma_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Curso:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=5)
    curso_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    curso_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

    # Configurar pesos da grid
    main_frame.grid_columnconfigure(1, weight=1)

    # Frame dos botões
    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

    def adicionar_aluno():
        nome = nome_entry.get().strip()
        ra = ra_entry.get().strip()
        turma = turma_entry.get().strip()
        curso = curso_entry.get().strip()

        if not nome or not ra or not turma or not curso:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        alunos = carregar_alunos()
        alunos.append({
            "nome": nome,
            "RA": ra,
            "turma": turma,
            "curso": curso
        })
        salvar_alunos(alunos)

        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()
            listar_alunos(parent_window)

    def voltar_menu():
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    btn_add_aluno = tk.Button(btn_frame, text="Adicionar Aluno", bg="#4CAF50", fg="white",
                             font=("Arial", 10, "bold"), relief="raised", width=15,
                             command=adicionar_aluno)
    btn_add_aluno.pack(side="left", padx=5)

    btn_voltar = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                          font=("Arial", 10, "bold"), relief="raised", width=15,
                          command=voltar_menu)
    btn_voltar.pack(side="left", padx=5)

    # Enter aciona o botão
    nome_entry.bind("<Return>", lambda event: adicionar_aluno())
    ra_entry.bind("<Return>", lambda event: adicionar_aluno())
    turma_entry.bind("<Return>", lambda event: adicionar_aluno())
    curso_entry.bind("<Return>", lambda event: adicionar_aluno())

# ===================== TELA DE DISCIPLINAS =====================
def listar_disciplinas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    disciplinas = carregar_disciplinas()
    dados_formatados = []
    for disc in disciplinas:
        dados_formatados.append({
            "nome": disc.get('nome', '-'),
            "codigo": disc.get('codigo', '-'),
            "professor": disc.get('professor', '-'),
            "carga_horaria": f"{disc.get('carga_horaria', '-')}h"
        })
    
    criar_janela_listagem(
        "Disciplinas Cadastradas",
        dados_formatados,
        ["Nome", "Código", "Professor", "Carga Horária"],
        [200, 100, 150, 120],
        parent_window
    )

def abrir_tela_disciplinas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Disciplina")
    janela_cadastro.geometry("500x450")
    janela_cadastro.config(bg="#dcdcdc")

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Disciplina", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Nome:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
    nome_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    nome_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Código:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
    codigo_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    codigo_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Professor:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
    professor_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    professor_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Carga Horária (h):", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=5)
    carga_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    carga_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

    def adicionar_disciplina():
        nome = nome_entry.get().strip()
        codigo = codigo_entry.get().strip()
        professor = professor_entry.get().strip()
        carga = carga_entry.get().strip()

        if not nome or not codigo or not professor or not carga:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        disciplinas = carregar_disciplinas()
        disciplinas.append({
            "nome": nome,
            "codigo": codigo,
            "professor": professor,
            "carga_horaria": carga
        })
        salvar_disciplinas(disciplinas)

        messagebox.showinfo("Sucesso", "Disciplina cadastrada com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()
            listar_disciplinas(parent_window)

    def voltar_menu():
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    btn_add_disciplina = tk.Button(btn_frame, text="Adicionar Disciplina", bg="#4CAF50", fg="white",
                                  font=("Arial", 10, "bold"), relief="raised", width=15,
                                  command=adicionar_disciplina)
    btn_add_disciplina.pack(side="left", padx=5)

    btn_voltar = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                          font=("Arial", 10, "bold"), relief="raised", width=15,
                          command=voltar_menu)
    btn_voltar.pack(side="left", padx=5)

    nome_entry.bind("<Return>", lambda event: adicionar_disciplina())
    codigo_entry.bind("<Return>", lambda event: adicionar_disciplina())
    professor_entry.bind("<Return>", lambda event: adicionar_disciplina())
    carga_entry.bind("<Return>", lambda event: adicionar_disciplina())

# ===================== TELA DE NOTAS =====================
def listar_notas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    notas = carregar_notas()
    dados_formatados = []
    for nota in notas:
        dados_formatados.append({
            "aluno": nota.get('aluno', '-'),
            "turma": nota.get('turma', '-'),
            "disciplina": nota.get('disciplina', '-'),
            "nota": nota.get('nota', '-')
        })
    
    criar_janela_listagem(
        "Notas Cadastradas",
        dados_formatados,
        ["Aluno", "Turma", "Disciplina", "Nota"],
        [250, 100, 150, 100],
        parent_window
    )

def abrir_tela_notas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Nota")
    janela_cadastro.geometry("500x450")
    janela_cadastro.config(bg="#dcdcdc")

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Nota", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Aluno:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
    alunos = [a.get('nome') for a in carregar_alunos()]
    aluno_combobox = ttk.Combobox(main_frame, values=alunos, width=27, font=("Arial", 10))
    aluno_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Turma:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
    turmas = list({a.get('turma') for a in carregar_alunos()})
    turma_combobox = ttk.Combobox(main_frame, values=turmas, width=27, font=("Arial", 10))
    turma_combobox.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Disciplina:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
    disciplinas = [d.get('nome') for d in carregar_disciplinas()]
    disciplina_combobox = ttk.Combobox(main_frame, values=disciplinas, width=27, font=("Arial", 10))
    disciplina_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(main_frame, text="Nota:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=5)
    nota_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
    nota_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

    def adicionar_nota():
        aluno = aluno_combobox.get().strip()
        turma = turma_combobox.get().strip()
        disciplina = disciplina_combobox.get().strip()
        nota = nota_entry.get().strip()

        if not aluno or not turma or not disciplina or not nota:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        notas = carregar_notas()
        notas.append({
            "aluno": aluno,
            "turma": turma,
            "disciplina": disciplina,
            "nota": nota
        })
        salvar_notas(notas)

        messagebox.showinfo("Sucesso", "Nota cadastrada com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()
            listar_notas(parent_window)

    def voltar_menu():
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    btn_add_nota = tk.Button(btn_frame, text="Adicionar Nota", bg="#4CAF50", fg="white",
                            font=("Arial", 10, "bold"), relief="raised", width=15,
                            command=adicionar_nota)
    btn_add_nota.pack(side="left", padx=5)

    btn_voltar = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                          font=("Arial", 10, "bold"), relief="raised", width=15,
                          command=voltar_menu)
    btn_voltar.pack(side="left", padx=5)

    aluno_combobox.bind("<Return>", lambda event: adicionar_nota())
    turma_combobox.bind("<Return>", lambda event: adicionar_nota())
    disciplina_combobox.bind("<Return>", lambda event: adicionar_nota())
    nota_entry.bind("<Return>", lambda event: adicionar_nota())
# ===================== TELA DE FALTAS =====================
def listar_faltas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    faltas = carregar_faltas()
    dados_formatados = []
    for falta in faltas:
        dados_formatados.append({
            "aluno": falta.get('aluno', '-'),
            "ra": falta.get('ra', '-'),
            "disciplina": falta.get('disciplina', '-'),
            "data": falta.get('data', '-'),
            "quantidade": falta.get('quantidade', '-')
        })
    
    criar_janela_listagem(
        "Faltas Cadastradas",
        dados_formatados,
        ["Aluno", "RA", "Disciplina", "Data", "Quantidade"],
        [200, 100, 150, 100, 100],
        parent_window
    )

def abrir_tela_faltas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Faltas")
    janela_cadastro.geometry("500x550")
    janela_cadastro.config(bg="#dcdcdc")
    janela_cadastro.resizable(False, False)

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Faltas", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Aluno:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
    alunos_data = carregar_alunos()
    alunos = [a.get('nome') for a in alunos_data]
    aluno_combobox = ttk.Combobox(main_frame, values=alunos, width=28, font=("Arial", 10))
    aluno_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=8)

    tk.Label(main_frame, text="RA:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
    ras = [a.get('RA') for a in alunos_data]
    ra_combobox = ttk.Combobox(main_frame, values=ras, width=28, font=("Arial", 10))
    ra_combobox.grid(row=2, column=1, sticky="ew", padx=10, pady=8)

    # Atualizar RA quando selecionar aluno
    def atualizar_ra(event):
        selected_aluno = aluno_combobox.get()
        for aluno in alunos_data:
            if aluno.get('nome') == selected_aluno:
                ra_combobox.set(aluno.get('RA'))
                break

    aluno_combobox.bind('<<ComboboxSelected>>', atualizar_ra)

    tk.Label(main_frame, text="Disciplina:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
    disciplinas = [d.get('nome') for d in carregar_disciplinas()]
    disciplina_combobox = ttk.Combobox(main_frame, values=disciplinas, width=28, font=("Arial", 10))
    disciplina_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=8)

    # Frame para data com calendário
    data_frame = tk.Frame(main_frame, bg="#dcdcdc")
    data_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=8)
    data_frame.grid_columnconfigure(1, weight=1)

    tk.Label(data_frame, text="Data:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")

    # Campo de entrada para data - MESMA LARGURA dos outros campos
    data_entry = ttk.Entry(data_frame, width=28, font=("Arial", 10))
    data_entry.grid(row=0, column=1, sticky="ew", padx=(10, 5), pady=8)
    data_entry.insert(0, "DD/MM/AAAA")

    # Função para limpar o placeholder quando o campo ganhar foco
    def limpar_placeholder(event):
        if data_entry.get() == "DD/MM/AAAA":
            data_entry.delete(0, tk.END)
            data_entry.config(foreground="black")

    # Função para restaurar o placeholder se estiver vazio
    def restaurar_placeholder(event):
        if data_entry.get() == "":
            data_entry.insert(0, "DD/MM/AAAA")
            data_entry.config(foreground="gray")

    # Configurar os eventos de foco
    data_entry.bind("<FocusIn>", limpar_placeholder)
    data_entry.bind("<FocusOut>", restaurar_placeholder)

    # Configurar cor inicial do placeholder
    data_entry.config(foreground="gray")

    # Botão para abrir calendário
    def abrir_calendario():
        calendario_janela = tk.Toplevel(janela_cadastro)
        calendario_janela.title("Selecionar Data")
        calendario_janela.geometry("300x280")
        calendario_janela.configure(bg="#dcdcdc")
        calendario_janela.transient(janela_cadastro)
        calendario_janela.grab_set()

        # Frame do calendário
        cal_frame = tk.Frame(calendario_janela, bg="#dcdcdc")
        cal_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Ano e mês atual
        import datetime
        hoje = datetime.datetime.now()
        ano_var = tk.IntVar(value=hoje.year)
        mes_var = tk.IntVar(value=hoje.month)

        # Frame de controle (ano e mês)
        controle_frame = tk.Frame(cal_frame, bg="#dcdcdc")
        controle_frame.pack(fill="x", pady=(0, 10))

        # Botão mês anterior
        def mes_anterior():
            mes = mes_var.get()
            ano = ano_var.get()
            if mes == 1:
                mes_var.set(12)
                ano_var.set(ano - 1)
            else:
                mes_var.set(mes - 1)
            atualizar_calendario()

        btn_anterior = tk.Button(controle_frame, text="◀", bg="#3498db", fg="white",
                                font=("Arial", 10, "bold"), command=mes_anterior)
        btn_anterior.pack(side="left", padx=5)

        # Label do mês/ano
        mes_ano_label = tk.Label(controle_frame, bg="#dcdcdc", font=("Arial", 12, "bold"))
        mes_ano_label.pack(side="left", expand=True)

        # Botão próximo mês
        def proximo_mes():
            mes = mes_var.get()
            ano = ano_var.get()
            if mes == 12:
                mes_var.set(1)
                ano_var.set(ano + 1)
            else:
                mes_var.set(mes + 1)
            atualizar_calendario()

        btn_proximo = tk.Button(controle_frame, text="▶", bg="#3498db", fg="white",
                               font=("Arial", 10, "bold"), command=proximo_mes)
        btn_proximo.pack(side="right", padx=5)

        # Frame dos dias da semana
        dias_semana_frame = tk.Frame(cal_frame, bg="#dcdcdc")
        dias_semana_frame.pack(fill="x")
        
        dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
        for i, dia in enumerate(dias_semana):
            tk.Label(dias_semana_frame, text=dia, bg="#dcdcdc", 
                    font=("Arial", 9, "bold"), width=4).grid(row=0, column=i, padx=2, pady=2)

        # Frame dos dias do mês
        dias_frame = tk.Frame(cal_frame, bg="#dcdcdc")
        dias_frame.pack(fill="both", expand=True)

        def atualizar_calendario():
            # Limpar dias anteriores
            for widget in dias_frame.winfo_children():
                widget.destroy()

            # Atualizar label do mês/ano
            meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
            mes_ano_label.config(text=f"{meses[mes_var.get()]} {ano_var.get()}")

            # Calcular primeiro dia do mês
            primeiro_dia = datetime.datetime(ano_var.get(), mes_var.get(), 1)
            dia_semana = primeiro_dia.weekday()

            # Ajustar para domingo como primeiro dia (0=domingo, 6=sábado)
            if dia_semana == 6:  # Se for domingo
                dia_semana = 0
            else:
                dia_semana += 1

            # Calcular número de dias no mês
            if mes_var.get() == 12:
                prox_mes = datetime.datetime(ano_var.get() + 1, 1, 1)
            else:
                prox_mes = datetime.datetime(ano_var.get(), mes_var.get() + 1, 1)
            ultimo_dia = prox_mes - datetime.timedelta(days=1)
            num_dias = ultimo_dia.day

            # Preencher dias vazios no início
            linha = 1
            coluna = 0
            for i in range(dia_semana):
                tk.Label(dias_frame, text="", bg="#dcdcdc", width=4).grid(row=linha, column=coluna, padx=2, pady=2)
                coluna += 1

            # Preencher os dias do mês
            for dia in range(1, num_dias + 1):
                def criar_comando(d):
                    return lambda: selecionar_dia(d)
                
                btn_dia = tk.Button(dias_frame, text=str(dia), bg="white", fg="black",
                                  font=("Arial", 9), width=4, relief="raised",
                                  command=criar_comando(dia))
                
                # Destacar o dia atual
                if (dia == hoje.day and mes_var.get() == hoje.month and 
                    ano_var.get() == hoje.year):
                    btn_dia.config(bg="#e74c3c", fg="white")
                
                btn_dia.grid(row=linha, column=coluna, padx=2, pady=2)
                coluna += 1
                
                if coluna > 6:  # Sábado
                    coluna = 0
                    linha += 1

        def selecionar_dia(dia):
            data_str = f"{dia:02d}/{mes_var.get():02d}/{ano_var.get()}"
            data_entry.delete(0, tk.END)  # Limpa completamente o campo
            data_entry.insert(0, data_str)  # Insere apenas a data selecionada
            data_entry.config(foreground="black")  # Muda a cor para preto
            calendario_janela.destroy()

        # Botão para hoje
        def selecionar_hoje():
            data_str = f"{hoje.day:02d}/{hoje.month:02d}/{hoje.year}"
            data_entry.delete(0, tk.END)  # Limpa completamente o campo
            data_entry.insert(0, data_str)  # Insere apenas a data de hoje
            data_entry.config(foreground="black")  # Muda a cor para preto
            calendario_janela.destroy()

        btn_hoje = tk.Button(cal_frame, text="Hoje", bg="#4CAF50", fg="white",
                           font=("Arial", 10, "bold"), command=selecionar_hoje)
        btn_hoje.pack(pady=10)

        # Inicializar calendário
        atualizar_calendario()

    btn_calendario = tk.Button(data_frame, text="📅", bg="#3498db", fg="white",
                              font=("Arial", 12), relief="raised", width=3,
                              command=abrir_calendario)
    btn_calendario.grid(row=0, column=2, padx=(5, 0))

    # Função para formatar data (manter para digitação manual)
    def formatar_data(event=None):
        texto = data_entry.get()
        
        # Se for o placeholder, não formata
        if texto == "DD/MM/AAAA":
            return
        
        texto = texto.replace("/", "").replace("-", "")
        
        if len(texto) >= 2:
            texto = texto[:2] + "/" + texto[2:]
        if len(texto) >= 5:
            texto = texto[:5] + "/" + texto[5:]
        if len(texto) > 10:
            texto = texto[:10]
        
        data_entry.delete(0, tk.END)
        data_entry.insert(0, texto)
        data_entry.config(foreground="black")  # Muda para preto quando usuário digita

    data_entry.bind("<KeyRelease>", formatar_data)

    tk.Label(main_frame, text="Quantidade:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="w", pady=8)
    quantidade_entry = ttk.Entry(main_frame, width=28, font=("Arial", 10))
    quantidade_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=8)

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=6, column=0, columnspan=2, pady=25)

    def adicionar_falta():
        aluno = aluno_combobox.get().strip()
        ra = ra_combobox.get().strip()
        disciplina = disciplina_combobox.get().strip()
        data = data_entry.get().strip()
        quantidade = quantidade_entry.get().strip()

        if not aluno or not ra or not disciplina or not data or not quantidade:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        if data == "DD/MM/AAAA" or len(data) != 10 or data.count("/") != 2:
            messagebox.showwarning("Data inválida", "Selecione ou digite uma data válida no formato DD/MM/AAAA")
            return

        try:
            qtd = int(quantidade)
            if qtd <= 0:
                messagebox.showwarning("Quantidade inválida", "A quantidade deve ser maior que zero")
                return
        except ValueError:
            messagebox.showwarning("Quantidade inválida", "Digite um número válido para a quantidade")
            return

        faltas = carregar_faltas()
        faltas.append({
            "aluno": aluno,
            "ra": ra,
            "disciplina": disciplina,
            "data": data,
            "quantidade": quantidade
        })
        salvar_faltas(faltas)

        messagebox.showinfo("Sucesso", "Falta cadastrada com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()
            listar_faltas(parent_window)

    def voltar_menu():
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    # Função para criar botões com hover personalizado
    def criar_botao_hover(parent, texto, cor_normal, comando=None, width=15):
        btn = tk.Button(parent, text=texto, bg=cor_normal, fg="white",
                       font=("Arial", 10, "bold"), relief="raised", width=width,
                       command=comando)
        
        # Configurar hover effects - verde claro fixo e negrito
        def on_enter(e):
            btn.config(bg="#90EE90", font=("Arial", 10, "bold"))  # Verde clarinho e negrito
        
        def on_leave(e):
            btn.config(bg=cor_normal, font=("Arial", 10, "bold"))  # Volta à cor normal, mantém negrito
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    btn_add_falta = criar_botao_hover(btn_frame, "Adicionar Falta", "#4CAF50", adicionar_falta)
    btn_add_falta.pack(side="left", padx=10)

    btn_voltar = criar_botao_hover(btn_frame, "Voltar ao Menu", "#3498db", voltar_menu)
    btn_voltar.pack(side="left", padx=10)

    # Bind Enter para todos os campos
    aluno_combobox.bind("<Return>", lambda event: adicionar_falta())
    ra_combobox.bind("<Return>", lambda event: adicionar_falta())
    disciplina_combobox.bind("<Return>", lambda event: adicionar_falta())
    data_entry.bind("<Return>", lambda event: adicionar_falta())
    quantidade_entry.bind("<Return>", lambda event: adicionar_falta())

    # Focar no primeiro campo
    aluno_combobox.focus_set()
# ===================== TELA ADMIN =====================
def abrir_tela_admin():
    tela_admin = tk.Tk()
    tela_admin.title("Painel Administrativo")
    tela_admin.geometry("550x550")
    tela_admin.configure(bg="#ecf0f1")

    def voltar_login():
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            tela_admin.destroy()

    # Cabeçalho
    header = tk.Frame(tela_admin, bg="#ecf0f1")
    header.pack(fill="x", pady=10, padx=10)

    bem_vindo_label = tk.Label(header, text="Bem-vindo(a), Admin",
                               bg=header.cget("bg"), bd=0, relief="flat",
                               font=("Arial", 16, "bold"))
    bem_vindo_label.pack(side="left")

    user_icon_path = r"PROJETO_TKINTER\user.png"
    try:
        user_img = Image.open(user_icon_path)
        user_img = user_img.resize((40, 40), Image.Resampling.LANCZOS)
        user_icon = ImageTk.PhotoImage(user_img)
    except:
        user_icon = None

    btn_logout = tk.Button(header, text="Logout", image=user_icon, compound="left",
                           bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                           command=voltar_login, relief="flat")
    btn_logout.image = user_icon
    btn_logout.pack(side="right")

    # Container do menu
    frame_menu = tk.Frame(tela_admin, bg="#ecf0f1")
    frame_menu.pack(expand=True)

    def criar_botao_menu(cor, texto, icone, comando):
        # Criar cores para hover
        cor_normal = cor
        cor_hover = "#90EE90"  # Verde clarinho como solicitado
        
        btn = tk.Button(frame_menu, bg=cor_normal, fg="white", font=("Arial", 12),
                        text=texto, compound="top", relief="flat", width=12, height=6, 
                        command=comando)
        
        # Configurar hover effects - texto sempre visível
        def on_enter(e):
            btn.config(bg=cor_hover, font=("Arial", 12, "bold"))  # Fica em negrito no hover
        
        def on_leave(e):
            btn.config(bg=cor_normal, font=("Arial", 12))  # Volta ao normal
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        if icone:
            try:
                img = Image.open(icone)
                max_size = 50
                img_ratio = img.width / img.height
                if img.width > max_size:
                    img = img.resize((max_size, int(max_size / img_ratio)), Image.Resampling.LANCZOS)
                if img.height > max_size:
                    img = img.resize((int(max_size * img_ratio), max_size), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)
                btn.config(image=img_tk)
                btn.image = img_tk
            except Exception as e:
                print(f"Erro ao carregar ícone {icone}: {e}")
        return btn

    # Caminhos dos ícones
    icone_aluno = r"PROJETO_TKINTER\aluno.png"
    icone_disciplina = r"PROJETO_TKINTER\disciplina.png"
    icone_notas = r"PROJETO_TKINTER\notas.png"
    icone_faltas = r"PROJETO_TKINTER\faltas.png"
    icone_config = r"PROJETO_TKINTER\config.png"

    def abrir_configuracoes():
        config_janela = tk.Toplevel(tela_admin)
        config_janela.title("Configurações")
        config_janela.geometry("300x200")
        config_janela.configure(bg="#ecf0f1")

        tk.Label(config_janela, text="Alterar cor de fundo", bg="#ecf0f1", font=("Arial", 12, "bold")).pack(pady=10)

        def mudar_cor_fundo():
            cor = color_entry.get().strip()
            if cor:
                tela_admin.configure(bg=cor)
                header.configure(bg=cor)
                frame_menu.configure(bg=cor)
                bem_vindo_label.configure(bg=cor)

        def modo_escuro():
            tela_admin.configure(bg="#2c3e50")
            header.configure(bg="#2c3e50")
            frame_menu.configure(bg="#2c3e50")
            bem_vindo_label.configure(bg="#2c3e50", fg="white")

        color_entry = ttk.Entry(config_janela)
        color_entry.pack(pady=5)
        ttk.Button(config_janela, text="Aplicar cor", command=mudar_cor_fundo).pack(pady=5)
        ttk.Button(config_janela, text="Modo Escuro", command=modo_escuro).pack(pady=5)

    # Criando botões do menu
    btn_aluno = criar_botao_menu("#1abc9c", "Alunos", icone_aluno, lambda: listar_alunos(tela_admin))
    btn_disciplina = criar_botao_menu("#2ecc71", "Disciplinas", icone_disciplina, lambda: listar_disciplinas(tela_admin))
    btn_notas = criar_botao_menu("#3498db", "Notas", icone_notas, lambda: listar_notas(tela_admin))
    btn_faltas = criar_botao_menu("#e67e22", "Faltas", icone_faltas, lambda: listar_faltas(tela_admin))
    btn_config = criar_botao_menu("#9b59b6", "Configurações", icone_config, abrir_configuracoes)

    # Posicionando os botões em grid 3x2
    btn_aluno.grid(row=0, column=0, padx=5, pady=5)
    btn_disciplina.grid(row=0, column=1, padx=5, pady=5)
    btn_notas.grid(row=1, column=0, padx=5, pady=5)
    btn_faltas.grid(row=1, column=1, padx=5, pady=5)
    btn_config.grid(row=2, column=0, padx=5, pady=5)

    tela_admin.mainloop()

# ===================== TELA DO ALUNO =====================
def abrir_tela_aluno(email_usuario):
    # ===================== FUNÇÃO PARA NORMALIZAR TEXTOS =====================
    def normalizar(texto):
        """Remove acentos e coloca em minúsculas"""
        if not texto:
            return ""
        return ''.join(c for c in unicodedata.normalize('NFD', texto)
                       if unicodedata.category(c) != 'Mn').lower()

    # ===================== INÍCIO DA TELA =====================
    tela_aluno = tk.Tk()
    tela_aluno.title("Minhas Notas")
    tela_aluno.geometry("800x600")
    tela_aluno.configure(bg="#ecf0f1")

    # ===================== FUNÇÃO SAIR =====================
    def confirmar_sair():
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair e voltar ao login?")
        if resposta:
            tela_aluno.destroy()
            main_login_window()

    # ===================== CABEÇALHO =====================
    header = tk.Frame(tela_aluno, bg="#ecf0f1")
    header.pack(fill="x", pady=10, padx=20)

    bem_vindo = tk.Label(header, text="Minhas notas", bg=header.cget("bg"),
                         font=("Arial", 20, "bold"))
    bem_vindo.pack(side="left")

    user_icon_path = r"PROJETO_TKINTER\user.png"
    try:
        user_img = Image.open(user_icon_path).resize((35, 35), Image.Resampling.LANCZOS)
        user_icon = ImageTk.PhotoImage(user_img)
    except:
        user_icon = None

    btn_logout = tk.Button(header, text="Logout", image=user_icon, compound="left",
                           bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                           command=confirmar_sair, relief="flat")
    btn_logout.image = user_icon
    btn_logout.pack(side="right")

    # ===================== CONTAINER PRINCIPAL =====================
    main_container = tk.Frame(tela_aluno, bg="#ecf0f1")
    main_container.pack(fill="both", expand=True, padx=20, pady=10)

    # ===================== CARREGAR DADOS =====================
    notas = carregar_notas()
    disciplinas = carregar_disciplinas()
    alunos = carregar_alunos()
    faltas = carregar_faltas()

    # ===================== IDENTIFICAR ALUNO =====================
    nome_aluno = None
    turma_aluno = None
    ra_aluno = None
    for a in alunos:
        if a.get("RA", "").strip().lower() == email_usuario.strip().lower() or \
           a.get("email", "").strip().lower() == email_usuario.strip().lower():
            nome_aluno = a.get("nome")
            turma_aluno = a.get("turma")
            ra_aluno = a.get("RA")
            break

    # ===================== FUNÇÃO FALTAS =====================
    def calcular_faltas_disciplina(disciplina_nome):
        total_faltas = 0
        for falta in faltas:
            if (falta.get("aluno", "").strip().lower() == nome_aluno.strip().lower() or \
                falta.get("ra", "").strip().lower() == ra_aluno.strip().lower()) and \
               falta.get("disciplina", "").strip().lower() == disciplina_nome.strip().lower():
                try:
                    total_faltas += int(falta.get("quantidade", 0))
                except:
                    pass
        return str(total_faltas)

    # ===================== MONTAR LISTA DE DISCIPLINAS =====================
    disciplinas_aluno = []
    for nota in notas:
        aluno_da_nota = nota.get("aluno") or nota.get("nome")
        turma_da_nota = nota.get("turma", "")

        if aluno_da_nota and nome_aluno and turma_aluno and \
           aluno_da_nota.strip().lower() == nome_aluno.strip().lower() and \
           turma_da_nota.strip().lower() == turma_aluno.strip().lower():

            disciplina_nome = nota.get("disciplina") or "-"
            nota_val = nota.get("nota") or "-"

            # 🔹 Busca inteligente pelo professor
            professor = "-"
            disciplina_normalizada = normalizar(disciplina_nome)

            for disc in disciplinas:
                nome_disciplina = disc.get("nome", "")
                if normalizar(nome_disciplina) in disciplina_normalizada or \
                   disciplina_normalizada in normalizar(nome_disciplina):
                    professor = disc.get("professor", "-")
                    break

            total_faltas = calcular_faltas_disciplina(disciplina_nome)

            status = "Cursando"
            if nota_val != "-":
                try:
                    nota_float = float(nota_val)
                    if nota_float >= 6.0:
                        status = "Aprovado"
                    else:
                        status = "Reprovado"
                except:
                    status = "Cursando"

            disciplinas_aluno.append({
                "nome": disciplina_nome,
                "professor": professor,
                "nota_final": nota_val,
                "faltas": total_faltas,
                "status": status,
                "turma": turma_aluno
            })

    # ===================== TABELA =====================
    if not disciplinas_aluno:
        lbl_vazio = tk.Label(main_container, text="Nenhuma disciplina encontrada para este usuário.",
                             bg="#ecf0f1", fg="gray", font=("Arial", 12))
        lbl_vazio.pack(pady=50)
    else:
        frame_tabela = tk.Frame(main_container, bg="#ecf0f1")
        frame_tabela.pack(fill="both", expand=True)

        style = ttk.Style()
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        style.configure("Treeview.Heading",
                        background="#4CAF50",
                        foreground="white",
                        font=("Arial", 10, "bold"))

        tree = ttk.Treeview(frame_tabela, columns=("Disciplina", "Professor", "Nota", "Faltas", "Status"),
                            show="headings", height=15)

        tree.heading("Disciplina", text="Disciplina")
        tree.heading("Professor", text="Professor")
        tree.heading("Nota", text="Nota")
        tree.heading("Faltas", text="Faltas")
        tree.heading("Status", text="Status")

        tree.column("Disciplina", width=200, anchor="center")
        tree.column("Professor", width=150, anchor="center")
        tree.column("Nota", width=100, anchor="center")
        tree.column("Faltas", width=100, anchor="center")
        tree.column("Status", width=100, anchor="center")

        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        for disc in disciplinas_aluno:
            tree.insert("", "end", values=(
                disc["nome"],
                disc["professor"],
                disc["nota_final"],
                disc["faltas"],
                disc["status"]
            ))

        tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

    # ===================== BOTÃO VOLTAR =====================
    btn_voltar = tk.Button(tela_aluno, text="Voltar ao Login", bg="#3498db", fg="white",
                           font=("Arial", 11, "bold"), relief="flat",
                           command=lambda: [tela_aluno.destroy(), main_login_window()])
    btn_voltar.pack(pady=10)

    tela_aluno.focus_force()
    tela_aluno.lift()
    tela_aluno.mainloop()


# ===================== LOGIN =====================
def main_login_window():
    global root, email_entry, senha_entry, login_btn, register_btn, fb_btn, google_btn, logo_img, logo, canvas, container_width, container_height

    root = tk.Tk()
    root.title("Login")
    root.geometry("800x600")
    root.configure(bg="#2c3e50")

    canvas = tk.Canvas(root, bg="#2c3e50", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    container_width = 350
    container_height = 450

    def round_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1, x2-radius, y1, x2, y1,
                  x2, y1+radius, x2, y2-radius, x2, y2,
                  x2-radius, y2, x1+radius, y2, x1, y2,
                  x1, y2-radius, x1, y1+radius, x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def container_wi():
        w = root.winfo_width()
        h = root.winfo_height()
        frame_x = (w - container_width) / 2
        frame_y = (h - container_height) / 2
        canvas.delete("container")
        round_rect(canvas, frame_x, frame_y, frame_x+container_width, frame_y+container_height,
                   radius=20, fill="#6a5acd", outline="#6a5acd", tags="container")
        return frame_x, frame_y

    frame_x, frame_y = container_wi()

    logo_path = "Logo Educacional B.A.N.O.L.L.png"
    try:
        img = Image.open(logo_path).resize((80, 80), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(img)
        logo = canvas.create_image(frame_x + container_width//2, frame_y + 60, image=logo_img, tags="logo")
    except:
        logo_img = None
        logo = None

    def create_entry(parent, placeholder="", is_password=False):
        entry = tk.Entry(parent, bd=0, bg="#ffffff", fg="gray", font=("Arial", 12))
        entry.insert(0, placeholder)
        if is_password:
            entry.config(show="")
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(fg="black")
                if is_password:
                    entry.config(show="*")
        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.config(fg="gray")
                if is_password:
                    entry.config(show="")
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        return entry

    email_entry = create_entry(root, placeholder="Email ou RA")
    senha_entry = create_entry(root, placeholder="Senha", is_password=True)

    def login():
        usuario = email_entry.get().strip()
        senha = senha_entry.get().strip()
        users = load_users()
        
        if usuario in users and users[usuario] == senha:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
            root.destroy()  # Fecha a tela de login
        
            if usuario == "admin":
                abrir_tela_admin()
            elif usuario == "H764113" or "@" in usuario:
                abrir_tela_aluno(usuario)
            elif usuario == "R8043H6" or "@" in usuario:
                abrir_tela_aluno(usuario)
            else:
                # Para outros usuários genéricos
                abrir_tela_aluno(usuario)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def register():
        usuario = email_entry.get().strip()
        senha = senha_entry.get().strip()
        users = load_users()
        if usuario in users:
            messagebox.showerror("Erro", "Usuário já existe!")
        else:
            users[usuario] = senha
            save_users(users)
            messagebox.showinfo("Sucesso", "Usuário cadastrado!")

    def google_login():
        webbrowser.open("https://accounts.google.com/signin/v2/identifier")

    def facebook_login():
        webbrowser.open("https://www.facebook.com/login.php")

    def create_button(parent, text, bg_color="#ffffff", fg_color="#6a5acd", command=None):
        btn = tk.Button(parent, text=text, bg=bg_color, fg=fg_color,
                         font=("Arial", 12, "bold"), bd=0, relief="flat", command=command)
        
        # Adicionar efeito hover visível
        def on_enter(e):
            btn.config(bg="#f0f0f0", font=("Arial", 12, "bold"))
        
        def on_leave(e):
            btn.config(bg=bg_color, font=("Arial", 12, "bold"))
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    login_btn = create_button(root, "Login", command=login)
    register_btn = create_button(root, "Cadastrar", bg_color="#27ae60", fg_color="white", command=register)
    fb_btn = create_button(root, "f", bg_color="#3b5998", fg_color="white", command=facebook_login)
    google_btn = create_button(root, "G", bg_color="#db4437", fg_color="white", command=google_login)

    def update_layout(event=None):
        frame_x, frame_y = container_wi()
        if logo:
            canvas.coords(logo, frame_x + container_width//2, frame_y + 60)
        email_entry.place(x=frame_x + 40, y=frame_y + 140, width=270, height=35)
        senha_entry.place(x=frame_x + 40, y=frame_y + 200, width=270, height=35)
        login_btn.place(x=frame_x + 40, y=frame_y + 260, width=130, height=40)
        register_btn.place(x=frame_x + 180, y=frame_y + 260, width=130, height=40)
        fb_btn.place(x=frame_x + int(container_width*0.25)-25, y=frame_y + 320, width=50, height=35)
        google_btn.place(x=frame_x + int(container_width*0.75)-25, y=frame_y + 320, width=50, height=35)

    root.bind("<Configure>", update_layout)
    update_layout()

    footer = tk.Label(root, text="© 2025 Minha Aplicação", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10))
    footer.pack(side="bottom", pady=10)

    email_entry.bind("<Return>", lambda e: login())
    senha_entry.bind("<Return>", lambda e: login())

    root.mainloop()
    
if __name__ == "__main__":
    inicializar_sistema()  
    main_login_window()