import tkinter as tk 
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
import json
import os
import webbrowser
import unicodedata
import datetime
import shutil

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
        notas = json.load(f)
    print(f"📊 Notas carregadas: {len(notas)} registros")  # DEBUG
    return notas

def salvar_notas(notas):
    with open(ARQUIVO_NOTAS, "w", encoding="utf-8") as f:
        json.dump(notas, f, ensure_ascii=False, indent=4)
    print(f"✅ Notas salvas: {len(notas)} registros")  # DEBUG

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

# ===================== ARQUIVO JSON (CONTEÚDOS) =====================
ARQUIVO_CONTEUDOS = "conteudos.json"

def carregar_conteudos():
    if not os.path.exists(ARQUIVO_CONTEUDOS):
        with open(ARQUIVO_CONTEUDOS, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
    with open(ARQUIVO_CONTEUDOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_conteudos(conteudos):
    with open(ARQUIVO_CONTEUDOS, "w", encoding="utf-8") as f:
        json.dump(conteudos, f, ensure_ascii=False, indent=4)

# ===================== FUNÇÃO PARA CADASTRAR USUÁRIOS PADRÃO =====================
def cadastrar_usuarios_padrao():
    """Cadastra usuários padrão se não existirem"""
    users = load_users()
    
    # AGORA usando códigos das matérias para professores
    usuarios_padrao = {
        "admin": "1234",
        "ENG001": "1234",  # Engenharia de Software - Prof. Raul
        "PYT002": "1234",  # Programação Python - Prof. Aldy
        "CPP003": "1234",  # Programação C++ - Prof. Rogerio
        "BD004": "1234",   # Banco de Dados
        "RED005": "1234",  # Redes de Computadores
        "SO006": "1234",   # Sistemas Operacionais
        "ED007": "1234",   # Estrutura de Dados
        "IA008": "1234",   # Inteligência Artificial
        "H764II3": "1234", # Aluno
        "R8043H6": "1234"  # Aluno
    }
    
    atualizado = False
    for usuario, senha in usuarios_padrao.items():
        if usuario not in users:
            users[usuario] = senha
            atualizado = True
            print(f"Usuário {usuario} cadastrado com senha {senha}")
    
    if atualizado:
        save_users(users)
        print("Usuários padrão cadastrados com sucesso!")

# ===================== INICIALIZAÇÃO DO SISTEMA =====================
def inicializar_sistema():
    """Garante que os dados iniciais estejam no sistema"""
    cadastrar_usuarios_padrao()  # ADICIONE ESTA LINHA
    
    alunos = carregar_alunos()
    disciplinas = carregar_disciplinas()
    
    # Adicionar aluno exemplo se não existir
    aluno_encontrado = any(aluno.get("RA") == "H764II3" for aluno in alunos)
    if not aluno_encontrado:
        alunos.append({
            "nome": "Bruno Augusto Gimenez Alves",
            "RA": "H764II3",
            "turma": "ADS2",
            "curso": "ADS - Análise e Desenvolvimento de Sistemas",
            "email": "H764II3"
        })
        salvar_alunos(alunos)
    
    # Adicionar disciplinas exemplo se não existirem
    disciplinas_exemplo = [
        {
            "nome": "Engenharia de Software", 
            "codigo": "ENG001", 
            "professor": "Raul", 
            "turma": "ADS2",
            "curso": "ADS - Análise e Desenvolvimento de Sistemas",
            "carga_horaria": "80"
        },
        {
            "nome": "Programação Python", 
            "codigo": "PYT002", 
            "professor": "Aldy", 
            "turma": "ADS2",
            "curso": "ADS - Análise e Desenvolvimento de Sistemas",
            "carga_horaria": "60"
        },
        {
            "nome": "Programação C++", 
            "codigo": "CPP003", 
            "professor": "Rogerio", 
            "turma": "ADS2",
            "curso": "ADS - Análise e Desenvolvimento de Sistemas",
            "carga_horaria": "70"
        }
    ]
    
    for disc in disciplinas_exemplo:
        if not any(d.get("codigo") == disc["codigo"] for d in disciplinas):
            disciplinas.append(disc)
    
    salvar_disciplinas(disciplinas)

# ===================== FUNÇÕES DE REMOÇÃO =====================
def remover_aluno(valores):
    """Remove um aluno baseado nos valores da linha selecionada"""
    alunos = carregar_alunos()
    nome, ra, turma, curso = valores
    
    # Encontrar e remover o aluno
    alunos = [aluno for aluno in alunos if not (
        aluno.get('nome', '') == nome and 
        aluno.get('RA', '') == ra and 
        aluno.get('turma', '') == turma and 
        aluno.get('curso', '') == curso
    )]
    
    salvar_alunos(alunos)

def remover_disciplina(valores):
    """Remove uma disciplina baseada nos valores da linha selecionada"""
    disciplinas = carregar_disciplinas()
    # Agora temos 6 valores: nome, codigo, professor, turma, curso, carga_horaria
    nome, codigo, professor, turma, curso, carga_horaria = valores
    
    # Remover 'h' da carga horária para comparação
    carga_horaria = carga_horaria.replace('h', '')
    
    # Encontrar e remover a disciplina
    disciplinas = [disc for disc in disciplinas if not (
        disc.get('nome', '') == nome and 
        disc.get('codigo', '') == codigo and 
        disc.get('professor', '') == professor and
        disc.get('turma', '') == turma and
        disc.get('curso', '') == curso and 
        disc.get('carga_horaria', '') == carga_horaria
    )]
    
    salvar_disciplinas(disciplinas)

def remover_nota(valores):
    """Remove uma nota baseada nos valores da linha selecionada"""
    notas = carregar_notas()
    aluno, turma, disciplina, np1, np2, media = valores
    
    # Encontrar e remover a nota
    notas = [n for n in notas if not (
        n.get('aluno', '') == aluno and 
        n.get('turma', '') == turma and 
        n.get('disciplina', '') == disciplina and 
        n.get('np1', '') == np1 and 
        n.get('np2', '') == np2
    )]
    
    salvar_notas(notas)

def remover_falta(valores):
    """Remove uma falta baseada nos valores da linha selecionada"""
    faltas = carregar_faltas()
    aluno, ra, disciplina, data, quantidade = valores
    
    # Encontrar e remover a falta
    faltas = [falta for falta in faltas if not (
        falta.get('aluno', '') == aluno and 
        falta.get('ra', '') == ra and 
        falta.get('disciplina', '') == disciplina and 
        falta.get('data', '') == data and 
        falta.get('quantidade', '') == quantidade
    )]
    
    salvar_faltas(faltas)

def remover_conteudo(valores):
    """Remove um conteúdo baseado nos valores da linha selecionada"""
    conteudos = carregar_conteudos()
    disciplina, titulo, descricao, data, arquivo, tipo = valores
    
    # Encontrar e remover o conteúdo
    conteudos = [cont for cont in conteudos if not (
        cont.get('disciplina', '') == disciplina and 
        cont.get('titulo', '') == titulo and 
        cont.get('data', '') == data
    )]
    
    salvar_conteudos(conteudos)

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
        tree = None
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
          foreground=[("selected", "#000000")])


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

    # Botão Remover Selecionado (apenas se houver dados)
    if dados and tree:
        def remover_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um item para remover.")
                return
            
            confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja remover o item selecionado?")
            if not confirmacao:
                return
            
            try:
                item_selecionado = selecionado[0]
                valores = tree.item(item_selecionado, 'values')
                
                if titulo == "Alunos Cadastrados":
                    remover_aluno(valores)
                elif titulo == "Turmas Cadastradas":
                    remover_disciplina(valores)
                elif titulo == "Notas Cadastradas":
                    remover_nota(valores)
                elif titulo == "Faltas Cadastradas":
                    remover_falta(valores)
                elif titulo == "Conteúdos Programáticos":
                    remover_conteudo(valores)
                
                tree.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Item removido com sucesso!")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover item: {str(e)}")

        btn_remover = tk.Button(btn_frame, text="Remover Selecionado", bg="#e74c3c", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=remover_selecionado)
        btn_remover.pack(side="left", padx=5)

    # Botão Adicionar (se aplicável)
    if titulo == "Alunos Cadastrados":
        btn_adicionar = tk.Button(btn_frame, text="Adicionar Novo Aluno", bg="#4CAF50", fg="white",
                                font=("Arial", 10, "bold"), relief="raised", 
                                command=lambda: [lista_janela.destroy(), abrir_tela_cadastro(parent_window)])
        btn_adicionar.pack(side="left", padx=5)
    elif titulo == "Turmas Cadastradas":
        btn_adicionar = tk.Button(btn_frame, text="Adicionar Nova Turma", bg="#4CAF50", fg="white",
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
    elif titulo == "Conteúdos Programáticos":
        btn_adicionar = tk.Button(btn_frame, text="Adicionar Conteúdo", bg="#4CAF50", fg="white",
                                font=("Arial", 10, "bold"), relief="raised", 
                                command=lambda: [lista_janela.destroy(), abrir_tela_conteudos(parent_window)])
        btn_adicionar.pack(side="left", padx=5)
    
    return lista_janela

# ===================== TELA DE CONTEÚDOS PROGRAMÁTICOS =====================
def listar_conteudos(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    conteudos = carregar_conteudos()
    
    lista_janela = tk.Toplevel()
    lista_janela.title("Conteúdos Programáticos")
    lista_janela.geometry("1200x700")
    lista_janela.configure(bg="#d9d9d9")

    # Frame do título e filtro
    header_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    header_frame.pack(fill="x", pady=10, padx=20)
    
    tk.Label(header_frame, text="Conteúdos Programáticos", bg="#d9d9d9",
             font=("Arial", 16, "bold")).pack(side="left")

    # Frame do filtro
    filter_frame = tk.Frame(header_frame, bg="#d9d9d9")
    filter_frame.pack(side="right")
    
    tk.Label(filter_frame, text="Filtrar por Disciplina:", bg="#d9d9d9", 
             font=("Arial", 10)).pack(side="left", padx=(20, 5))
    
    disciplinas_opcoes = ["Todas as Disciplinas"] + sorted(list({cont.get('disciplina', '') for cont in conteudos if cont.get('disciplina')}))
    disciplina_filter_var = tk.StringVar(value="Todas as Disciplinas")
    disciplina_filter = ttk.Combobox(filter_frame, textvariable=disciplina_filter_var, 
                                   values=disciplinas_opcoes, width=20, state="readonly")
    disciplina_filter.pack(side="left", padx=5)
    
    contador_label = tk.Label(header_frame, text=f"Total de conteúdos: {len(conteudos)}", 
                             bg="#d9d9d9", font=("Arial", 10))
    contador_label.pack(side="left", padx=20)

    # Frame da tabela
    frame_tabela = tk.Frame(lista_janela, bg="#d9d9d9")
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    if not conteudos:
        tk.Label(frame_tabela, text="Nenhum conteúdo cadastrado.",
                 bg="#d9d9d9", font=("Arial", 11)).pack()
        tree = None
    else:
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
                  foreground=[("selected", "#000000")])

        tree = ttk.Treeview(frame_tabela, 
                           columns=["Disciplina", "Título", "Descrição", "Data", "Arquivo", "Tipo"], 
                           show="headings", height=15)
        
        tree.heading("Disciplina", text="Disciplina")
        tree.heading("Título", text="Título")
        tree.heading("Descrição", text="Descrição")
        tree.heading("Data", text="Data")
        tree.heading("Arquivo", text="Arquivo")
        tree.heading("Tipo", text="Tipo")
        
        tree.column("Disciplina", width=150, anchor="center")
        tree.column("Título", width=200, anchor="center")
        tree.column("Descrição", width=250, anchor="center")
        tree.column("Data", width=100, anchor="center")
        tree.column("Arquivo", width=150, anchor="center")
        tree.column("Tipo", width=100, anchor="center")
        
        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        for cont in conteudos:
            tree.insert("", "end", values=(
                cont.get('disciplina', '-'),
                cont.get('titulo', '-'),
                cont.get('descricao', '-')[:50] + "..." if len(cont.get('descricao', '')) > 50 else cont.get('descricao', '-'),
                cont.get('data', '-'),
                cont.get('arquivo', '-'),
                cont.get('tipo', '-')
            ))
        
        tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Função para visualizar conteúdo completo
        def visualizar_conteudo():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um conteúdo para visualizar.")
                return
            
            item = selecionado[0]
            valores = tree.item(item, 'values')
            
            # Encontrar conteúdo completo
            conteudo_completo = None
            for cont in conteudos:
                if (cont.get('disciplina') == valores[0] and 
                    cont.get('titulo') == valores[1] and 
                    cont.get('data') == valores[3]):
                    conteudo_completo = cont
                    break
            
            if conteudo_completo:
                visualizar_janela = tk.Toplevel(lista_janela)
                visualizar_janela.title(f"Conteúdo: {valores[1]}")
                visualizar_janela.geometry("600x500")
                visualizar_janela.configure(bg="#dcdcdc")
                
                main_frame = tk.Frame(visualizar_janela, bg="#dcdcdc")
                main_frame.pack(fill="both", expand=True, padx=20, pady=20)
                
                tk.Label(main_frame, text=conteudo_completo.get('titulo', ''), 
                        bg="#dcdcdc", font=("Arial", 16, "bold")).pack(pady=(0, 10))
                
                info_frame = tk.Frame(main_frame, bg="#dcdcdc")
                info_frame.pack(fill="x", pady=5)
                
                tk.Label(info_frame, text=f"Disciplina: {conteudo_completo.get('disciplina', '')}", 
                        bg="#dcdcdc", font=("Arial", 11)).pack(anchor="w")
                tk.Label(info_frame, text=f"Data: {conteudo_completo.get('data', '')}", 
                        bg="#dcdcdc", font=("Arial", 11)).pack(anchor="w")
                tk.Label(info_frame, text=f"Tipo: {conteudo_completo.get('tipo', '')}", 
                        bg="#dcdcdc", font=("Arial", 11)).pack(anchor="w")
                
                # Frame da descrição com scrollbar
                desc_frame = tk.Frame(main_frame, bg="#dcdcdc")
                desc_frame.pack(fill="both", expand=True, pady=10)
                
                tk.Label(desc_frame, text="Descrição:", bg="#dcdcdc", 
                        font=("Arial", 12, "bold")).pack(anchor="w")
                
                desc_text = tk.Text(desc_frame, wrap="word", width=60, height=15,
                                  font=("Arial", 10), bg="white", relief="solid", bd=1)
                desc_scrollbar = ttk.Scrollbar(desc_frame, orient="vertical", command=desc_text.yview)
                desc_text.configure(yscrollcommand=desc_scrollbar.set)
                
                desc_text.insert("1.0", conteudo_completo.get('descricao', ''))
                desc_text.config(state="disabled")
                
                desc_text.pack(side="left", fill="both", expand=True)
                desc_scrollbar.pack(side="right", fill="y")
                
                # Botão para baixar arquivo
                if conteudo_completo.get('arquivo') and conteudo_completo.get('arquivo') != '-':
                    def baixar_arquivo():
                        arquivo_path = conteudo_completo.get('arquivo')
                        if os.path.exists(arquivo_path):
                            try:
                                # Abrir o arquivo com o programa padrão
                                os.startfile(arquivo_path)
                            except:
                                messagebox.showinfo("Arquivo", f"Arquivo: {arquivo_path}")
                        else:
                            messagebox.showwarning("Arquivo não encontrado", 
                                                 "O arquivo não foi encontrado no sistema.")
                    
                    btn_baixar = tk.Button(main_frame, text="📥 Abrir Arquivo", bg="#3498db", fg="white",
                                         font=("Arial", 10, "bold"), command=baixar_arquivo)
                    btn_baixar.pack(pady=10)
                
                btn_fechar = tk.Button(main_frame, text="Fechar", bg="#e74c3c", fg="white",
                                     font=("Arial", 10, "bold"), command=visualizar_janela.destroy)
                btn_fechar.pack(pady=5)

    # Frame dos botões
    btn_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    btn_frame.pack(pady=10)

    def voltar_menu():
        lista_janela.destroy()
        if parent_window:
            parent_window.deiconify()

    def aplicar_filtro():
        disciplina_selecionada = disciplina_filter_var.get()
        if disciplina_selecionada == "Todas as Disciplinas":
            conteudos_filtrados = conteudos
        else:
            conteudos_filtrados = [cont for cont in conteudos if cont.get('disciplina') == disciplina_selecionada]
        
        for item in tree.get_children():
            tree.delete(item)
            
        for cont in conteudos_filtrados:
            tree.insert("", "end", values=(
                cont.get('disciplina', '-'),
                cont.get('titulo', '-'),
                cont.get('descricao', '-')[:50] + "..." if len(cont.get('descricao', '')) > 50 else cont.get('descricao', '-'),
                cont.get('data', '-'),
                cont.get('arquivo', '-'),
                cont.get('tipo', '-')
            ))
        
        contador_label.config(text=f"Total de conteúdos: {len(conteudos_filtrados)}")

    # Botões principais
    btn_voltar_menu = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                              font=("Arial", 10, "bold"), command=voltar_menu)
    btn_voltar_menu.pack(side="left", padx=5)

    if conteudos and tree:
        btn_visualizar = tk.Button(btn_frame, text="Visualizar Conteúdo", bg="#f39c12", fg="white",
                                 font=("Arial", 10, "bold"), command=visualizar_conteudo)
        btn_visualizar.pack(side="left", padx=5)

        def remover_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um conteúdo para remover.")
                return
            
            confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja remover o conteúdo selecionado?")
            if not confirmacao:
                return
            
            try:
                item_selecionado = selecionado[0]
                valores = tree.item(item_selecionado, 'values')
                
                # Remover arquivo físico se existir
                conteudo_completo = None
                for cont in conteudos:
                    if (cont.get('disciplina') == valores[0] and 
                        cont.get('titulo') == valores[1] and 
                        cont.get('data') == valores[3]):
                        conteudo_completo = cont
                        break
                
                if conteudo_completo and conteudo_completo.get('arquivo') and conteudo_completo.get('arquivo') != '-':
                    try:
                        if os.path.exists(conteudo_completo.get('arquivo')):
                            os.remove(conteudo_completo.get('arquivo'))
                    except:
                        pass  # Se não conseguir remover o arquivo, continua
                
                # Remover do JSON
                conteudos_atualizados = [cont for cont in conteudos if not (
                    cont.get('disciplina', '') == valores[0] and 
                    cont.get('titulo', '') == valores[1] and 
                    cont.get('data', '') == valores[3]
                )]
                salvar_conteudos(conteudos_atualizados)
                
                tree.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Conteúdo removido com sucesso!")
                
                # Atualizar contador
                disciplina_atual = disciplina_filter_var.get()
                if disciplina_atual == "Todas as Disciplinas":
                    conteudos_restantes = carregar_conteudos()
                else:
                    conteudos_restantes = [cont for cont in carregar_conteudos() if cont.get('disciplina') == disciplina_atual]
                contador_label.config(text=f"Total de conteúdos: {len(conteudos_restantes)}")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover conteúdo: {str(e)}")

        btn_remover = tk.Button(btn_frame, text="Remover Selecionado", bg="#e74c3c", fg="white",
                              font=("Arial", 10, "bold"), command=remover_selecionado)
        btn_remover.pack(side="left", padx=5)

    btn_adicionar = tk.Button(btn_frame, text="Adicionar Conteúdo", bg="#4CAF50", fg="white",
                            font=("Arial", 10, "bold"), 
                            command=lambda: [lista_janela.destroy(), abrir_tela_conteudos(parent_window)])
    btn_adicionar.pack(side="left", padx=5)
    
    def limpar_filtro():
        disciplina_filter_var.set("Todas as Disciplinas")
        aplicar_filtro()

    btn_limpar = tk.Button(btn_frame, text="Limpar Filtro", bg="#f39c12", fg="white",
                          font=("Arial", 10, "bold"), command=limpar_filtro)
    btn_limpar.pack(side="left", padx=5)

    disciplina_filter.bind('<<ComboboxSelected>>', lambda event: aplicar_filtro())

    return lista_janela

# ===================== TELA DE CADASTRO DE CONTEÚDOS =====================
def abrir_tela_conteudos(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Conteúdo Programático")
    janela_cadastro.geometry("600x700")
    janela_cadastro.config(bg="#dcdcdc")
    janela_cadastro.resizable(False, False)

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Conteúdo Programático", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Disciplina:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
    disciplinas = [d.get('nome') for d in carregar_disciplinas()]
    disciplina_combobox = ttk.Combobox(main_frame, values=disciplinas, width=40, font=("Arial", 10))
    disciplina_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=8)
    disciplina_combobox.set("")

    tk.Label(main_frame, text="Título do Conteúdo:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
    titulo_entry = ttk.Entry(main_frame, width=40, font=("Arial", 10))
    titulo_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=8)

    tk.Label(main_frame, text="Tipo de Conteúdo:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
    tipo_opcoes = ["Aula Teórica", "Aula Prática", "Material de Estudo", "Exercícios", "Projeto", "Calendário", "Plano de Ensino"]
    tipo_combobox = ttk.Combobox(main_frame, values=tipo_opcoes, width=40, font=("Arial", 10))
    tipo_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=8)
    tipo_combobox.set("")

    # Frame para data
    data_frame = tk.Frame(main_frame, bg="#dcdcdc")
    data_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=8)
    data_frame.grid_columnconfigure(1, weight=1)

    tk.Label(data_frame, text="Data:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")

    data_entry = ttk.Entry(data_frame, width=40, font=("Arial", 10))
    data_entry.grid(row=0, column=1, sticky="ew", padx=(10, 5), pady=8)
    data_entry.insert(0, "DD/MM/AAAA")

    def limpar_placeholder(event):
        if data_entry.get() == "DD/MM/AAAA":
            data_entry.delete(0, tk.END)

    def restaurar_placeholder(event):
        if data_entry.get() == "":
            data_entry.insert(0, "DD/MM/AAAA")

    data_entry.bind("<FocusIn>", limpar_placeholder)
    data_entry.bind("<FocusOut>", restaurar_placeholder)

    def abrir_calendario():
        calendario_janela = tk.Toplevel(janela_cadastro)
        calendario_janela.title("Selecionar Data")
        calendario_janela.geometry("300x280")
        calendario_janela.configure(bg="#dcdcdc")
        calendario_janela.transient(janela_cadastro)
        calendario_janela.grab_set()

        cal_frame = tk.Frame(calendario_janela, bg="#dcdcdc")
        cal_frame.pack(padx=10, pady=10, fill="both", expand=True)

        hoje = datetime.datetime.now()
        ano_var = tk.IntVar(value=hoje.year)
        mes_var = tk.IntVar(value=hoje.month)

        controle_frame = tk.Frame(cal_frame, bg="#dcdcdc")
        controle_frame.pack(fill="x", pady=(0, 10))

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

        mes_ano_label = tk.Label(controle_frame, bg="#dcdcdc", font=("Arial", 12, "bold"))
        mes_ano_label.pack(side="left", expand=True)

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

        dias_semana_frame = tk.Frame(cal_frame, bg="#dcdcdc")
        dias_semana_frame.pack(fill="x")
        
        dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
        for i, dia in enumerate(dias_semana):
            tk.Label(dias_semana_frame, text=dia, bg="#dcdcdc", 
                    font=("Arial", 9, "bold"), width=4).grid(row=0, column=i, padx=2, pady=2)

        dias_frame = tk.Frame(cal_frame, bg="#dcdcdc")
        dias_frame.pack(fill="both", expand=True)

        def atualizar_calendario():
            for widget in dias_frame.winfo_children():
                widget.destroy()

            meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
            mes_ano_label.config(text=f"{meses[mes_var.get()]} {ano_var.get()}")

            primeiro_dia = datetime.datetime(ano_var.get(), mes_var.get(), 1)
            dia_semana = primeiro_dia.weekday()

            if dia_semana == 6:
                dia_semana = 0
            else:
                dia_semana += 1

            if mes_var.get() == 12:
                prox_mes = datetime.datetime(ano_var.get() + 1, 1, 1)
            else:
                prox_mes = datetime.datetime(ano_var.get(), mes_var.get() + 1, 1)
            ultimo_dia = prox_mes - datetime.timedelta(days=1)
            num_dias = ultimo_dia.day

            linha = 1
            coluna = 0
            for i in range(dia_semana):
                tk.Label(dias_frame, text="", bg="#dcdcdc", width=4).grid(row=linha, column=coluna, padx=2, pady=2)
                coluna += 1

            for dia in range(1, num_dias + 1):
                def criar_comando(d):
                    return lambda: selecionar_dia(d)
                
                btn_dia = tk.Button(dias_frame, text=str(dia), bg="white", fg="black",
                                  font=("Arial", 9), width=4, relief="raised",
                                  command=criar_comando(dia))
                
                if (dia == hoje.day and mes_var.get() == hoje.month and 
                    ano_var.get() == hoje.year):
                    btn_dia.config(bg="#e74c3c", fg="white")
                
                btn_dia.grid(row=linha, column=coluna, padx=2, pady=2)
                coluna += 1
                
                if coluna > 6:
                    coluna = 0
                    linha += 1

        def selecionar_dia(dia):
            data_str = f"{dia:02d}/{mes_var.get():02d}/{ano_var.get()}"
            data_entry.delete(0, tk.END)
            data_entry.insert(0, data_str)
            calendario_janela.destroy()

        def selecionar_hoje():
            data_str = f"{hoje.day:02d}/{hoje.month:02d}/{hoje.year}"
            data_entry.delete(0, tk.END)
            data_entry.insert(0, data_str)
            calendario_janela.destroy()

        btn_hoje = tk.Button(cal_frame, text="Hoje", bg="#4CAF50", fg="white",
                           font=("Arial", 10, "bold"), command=selecionar_hoje)
        btn_hoje.pack(pady=10)

        atualizar_calendario()

    btn_calendario = tk.Button(data_frame, text="📅", bg="#3498db", fg="white",
                              font=("Arial", 12), relief="raised", width=3,
                              command=abrir_calendario)
    btn_calendario.grid(row=0, column=2, padx=(5, 0))

    def formatar_data(event=None):
        texto = data_entry.get()
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

    data_entry.bind("<KeyRelease>", formatar_data)

    # Descrição
    tk.Label(main_frame, text="Descrição Detalhada:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="w", pady=8)
    
    descricao_frame = tk.Frame(main_frame, bg="#dcdcdc")
    descricao_frame.grid(row=5, column=1, sticky="ew", padx=10, pady=8)
    
    descricao_text = tk.Text(descricao_frame, wrap="word", width=40, height=8,
                           font=("Arial", 10), bg="white", relief="solid", bd=1)
    descricao_scrollbar = ttk.Scrollbar(descricao_frame, orient="vertical", command=descricao_text.yview)
    descricao_text.configure(yscrollcommand=descricao_scrollbar.set)
    
    descricao_text.pack(side="left", fill="both", expand=True)
    descricao_scrollbar.pack(side="right", fill="y")

    # Upload de arquivo
    arquivo_path = tk.StringVar()
    
    tk.Label(main_frame, text="Arquivo (PDF/Imagem):", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w", pady=8)
    
    arquivo_frame = tk.Frame(main_frame, bg="#dcdcdc")
    arquivo_frame.grid(row=6, column=1, sticky="ew", padx=10, pady=8)
    
    arquivo_entry = ttk.Entry(arquivo_frame, textvariable=arquivo_path, width=30, font=("Arial", 10))
    arquivo_entry.pack(side="left", fill="x", expand=True)
    
    def selecionar_arquivo():
        filetypes = [
            ("Documentos PDF", "*.pdf"),
            ("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("Documentos Word", "*.doc *.docx"),
            ("Todos os arquivos", "*.*")
        ]
        
        arquivo = filedialog.askopenfilename(
            title="Selecionar arquivo",
            filetypes=filetypes
        )
        
        if arquivo:
            arquivo_path.set(arquivo)
            
            # Criar pasta de uploads se não existir
            uploads_dir = "uploads"
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            
            # Copiar arquivo para pasta uploads
            filename = os.path.basename(arquivo)
            destino = os.path.join(uploads_dir, filename)
            shutil.copy2(arquivo, destino)
            arquivo_path.set(destino)

    btn_selecionar = tk.Button(arquivo_frame, text="📁 Selecionar", bg="#3498db", fg="white",
                             font=("Arial", 9, "bold"), command=selecionar_arquivo)
    btn_selecionar.pack(side="right", padx=(5, 0))

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=7, column=0, columnspan=2, pady=25)

    def adicionar_conteudo():
        disciplina = disciplina_combobox.get().strip()
        titulo = titulo_entry.get().strip()
        tipo = tipo_combobox.get().strip()
        data = data_entry.get().strip()
        descricao = descricao_text.get("1.0", "end-1c").strip()
        arquivo = arquivo_path.get().strip()

        if not disciplina or not titulo or not tipo or not data:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos obrigatórios!")
            return

        if data == "DD/MM/AAAA" or len(data) != 10 or data.count("/") != 2:
            messagebox.showwarning("Data inválida", "Selecione ou digite uma data válida no formato DD/MM/AAAA")
            return

        conteudos = carregar_conteudos()
        
        # Verificar se já existe conteúdo com mesmo título e disciplina
        conteudo_existente = any(
            cont.get('disciplina') == disciplina and 
            cont.get('titulo') == titulo 
            for cont in conteudos
        )
        
        if conteudo_existente:
            messagebox.showwarning("Conteúdo duplicado", "Já existe um conteúdo com este título para esta disciplina!")
            return

        novo_conteudo = {
            "disciplina": disciplina,
            "titulo": titulo,
            "tipo": tipo,
            "data": data,
            "descricao": descricao,
            "arquivo": arquivo if arquivo else "-",
            "data_cadastro": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        conteudos.append(novo_conteudo)
        salvar_conteudos(conteudos)

        messagebox.showinfo("Sucesso", "Conteúdo cadastrado com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()
            listar_conteudos(parent_window)

    def voltar_menu():
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    def criar_botao_hover(parent, texto, cor_normal, comando=None, width=15):
        btn = tk.Button(parent, text=texto, bg=cor_normal, fg="white",
                       font=("Arial", 10, "bold"), relief="raised", width=width,
                       command=comando)
        
        def on_enter(e):
            btn.config(bg="#90EE90", font=("Arial", 10, "bold"))
        
        def on_leave(e):
            btn.config(bg=cor_normal, font=("Arial", 10, "bold"))
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    btn_add_conteudo = criar_botao_hover(btn_frame, "Adicionar Conteúdo", "#4CAF50", adicionar_conteudo)
    btn_add_conteudo.pack(side="left", padx=10)

    btn_voltar = criar_botao_hover(btn_frame, "Voltar ao Menu", "#3498db", voltar_menu)
    btn_voltar.pack(side="left", padx=10)

    # Bind Enter para focar no próximo campo
    disciplina_combobox.bind("<Return>", lambda event: titulo_entry.focus())
    titulo_entry.bind("<Return>", lambda event: tipo_combobox.focus())
    tipo_combobox.bind("<Return>", lambda event: data_entry.focus())
    data_entry.bind("<Return>", lambda event: descricao_text.focus())

    disciplina_combobox.focus_set()

    return janela_cadastro

# ===================== TELA DE ALUNOS COM FILTRO =====================
def listar_alunos(parent_window=None):
    if parent_window:
        parent_window.withdraw()
    
    alunos = carregar_alunos()
    
    # Criar janela com filtro
    lista_janela = tk.Toplevel()
    lista_janela.title("Alunos Cadastrados")
    lista_janela.geometry("900x600")
    lista_janela.configure(bg="#d9d9d9")

    # Frame do título e filtro
    header_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    header_frame.pack(fill="x", pady=10, padx=20)
    
    tk.Label(header_frame, text="Alunos Cadastrados", bg="#d9d9d9",
             font=("Arial", 14, "bold")).pack(side="left")

    # Frame do filtro (lado direito)
    filter_frame = tk.Frame(header_frame, bg="#d9d9d9")
    filter_frame.pack(side="right")
    
    tk.Label(filter_frame, text="Filtrar por Turma:", bg="#d9d9d9", 
             font=("Arial", 10)).pack(side="left", padx=(20, 5))
    
    # Combobox para filtro de turma
    turmas_opcoes = ["Todas as Turmas"] + sorted(list({aluno.get('turma', '') for aluno in alunos if aluno.get('turma')}))
    turma_filter_var = tk.StringVar(value="Todas as Turmas")
    turma_filter = ttk.Combobox(filter_frame, textvariable=turma_filter_var, 
                               values=turmas_opcoes, width=15, state="readonly")
    turma_filter.pack(side="left", padx=5)
    
    # Label contador
    contador_label = tk.Label(header_frame, text=f"Total de alunos: {len(alunos)}", 
                             bg="#d9d9d9", font=("Arial", 10))
    contador_label.pack(side="left", padx=20)

    # Frame da tabela
    frame_tabela = tk.Frame(lista_janela, bg="#d9d9d9")
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    if not alunos:
        tk.Label(frame_tabela, text="Nenhum aluno cadastrado.",
                 bg="#d9d9d9", font=("Arial", 11)).pack()
        tree = None
    else:
        # Criar Treeview
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
                  foreground=[("selected", "#000000")])

        tree = ttk.Treeview(frame_tabela, columns=["Nome", "RA", "Turma", "Curso"], 
                           show="headings", height=15)
        
        # Definir headings
        tree.heading("Nome", text="Nome")
        tree.heading("RA", text="RA")
        tree.heading("Turma", text="Turma")
        tree.heading("Curso", text="Curso")
        
        # Definir larguras
        tree.column("Nome", width=300, anchor="center")
        tree.column("RA", width=120, anchor="center")
        tree.column("Turma", width=100, anchor="center")
        tree.column("Curso", width=150, anchor="center")
        
        # Adicionar scrollbars
        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Inserir dados iniciais
        for aluno in alunos:
            tree.insert("", "end", values=(
                aluno.get('nome', '-'),
                aluno.get('RA', '-'),
                aluno.get('turma', '-'),
                aluno.get('curso', '-')
            ))
        
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

    # Função para aplicar filtro
    def aplicar_filtro():
        turma_selecionada = turma_filter_var.get()
        if turma_selecionada == "Todas as Turmas":
            alunos_filtrados = alunos
        else:
            alunos_filtrados = [aluno for aluno in alunos if aluno.get('turma') == turma_selecionada]
        
        # Atualizar a tabela
        for item in tree.get_children():
            tree.delete(item)
            
        for aluno in alunos_filtrados:
            tree.insert("", "end", values=(
                aluno.get('nome', '-'),
                aluno.get('RA', '-'),
                aluno.get('turma', '-'),
                aluno.get('curso', '-')
            ))
        
        # Atualizar contador
        contador_label.config(text=f"Total de alunos: {len(alunos_filtrados)}")

    # Botão Voltar ao Menu
    btn_voltar_menu = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=voltar_menu)
    btn_voltar_menu.pack(side="left", padx=5)

    # Botão Remover Selecionado (apenas se houver dados)
    if alunos and tree:
        def remover_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um aluno para remover.")
                return
            
            confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja remover o aluno selecionado?")
            if not confirmacao:
                return
            
            try:
                item_selecionado = selecionado[0]
                valores = tree.item(item_selecionado, 'values')
                remover_aluno(valores)
                
                tree.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Aluno removido com sucesso!")
                
                # Atualizar contador
                turma_atual = turma_filter_var.get()
                if turma_atual == "Todas as Turmas":
                    alunos_restantes = carregar_alunos()
                else:
                    alunos_restantes = [aluno for aluno in carregar_alunos() if aluno.get('turma') == turma_atual]
                contador_label.config(text=f"Total de alunos: {len(alunos_restantes)}")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover aluno: {str(e)}")

        btn_remover = tk.Button(btn_frame, text="Remover Selecionado", bg="#e74c3c", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=remover_selecionado)
        btn_remover.pack(side="left", padx=5)

    # Botão Adicionar Novo Aluno
    btn_adicionar = tk.Button(btn_frame, text="Adicionar Novo Aluno", bg="#4CAF50", fg="white",
                            font=("Arial", 10, "bold"), relief="raised", 
                            command=lambda: [lista_janela.destroy(), abrir_tela_cadastro(parent_window)])
    btn_adicionar.pack(side="left", padx=5)
    
    # Botão Limpar Filtro
    def limpar_filtro():
        turma_filter_var.set("Todas as Turmas")
        aplicar_filtro()

    btn_limpar = tk.Button(btn_frame, text="Limpar Filtro", bg="#f39c12", fg="white",
                          font=("Arial", 10, "bold"), relief="raised", 
                          command=limpar_filtro)
    btn_limpar.pack(side="left", padx=5)

    # Aplicar filtro automaticamente quando selecionar uma turma
    turma_filter.bind('<<ComboboxSelected>>', lambda event: aplicar_filtro())

    return lista_janela

# ===================== TELA DE CADASTRO DE ALUNOS =====================
def abrir_tela_cadastro(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Aluno")
    janela_cadastro.geometry("500x450")
    janela_cadastro.config(bg="#dcdcdc")
    janela_cadastro.resizable(False, False)

    # Frame principal
    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título
    tk.Label(main_frame, text="Cadastro de Aluno", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Nome:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
    nome_entry = ttk.Entry(main_frame, width=28, font=("Arial", 10))
    nome_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=8)

    tk.Label(main_frame, text="RA:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
    ra_entry = ttk.Entry(main_frame, width=28, font=("Arial", 10))
    ra_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=8)

    tk.Label(main_frame, text="Turma:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
    
    # Combobox para Turma com opções pré-definidas
    turmas_opcoes = ["ADS1", "ADS2", "ADS3", "ADS4"]
    turma_combobox = ttk.Combobox(main_frame, values=turmas_opcoes, width=25, font=("Arial", 10))
    turma_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=8)
    turma_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Curso:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=8)
    
    # Combobox para Curso com opções pré-definidas
    cursos_opcoes = [
        "ADS - Análise e Desenvolvimento de Sistemas",
        "GTI - Gestão da Tecnologia da Informação", 
        "SI - Sistemas de Informação",
        "CC - Ciência da Computação",
        "EC - Engenharia da Computação",
        "RC - Redes de Computadores"
    ]
    curso_combobox = ttk.Combobox(main_frame, values=cursos_opcoes, width=25, font=("Arial", 10))
    curso_combobox.grid(row=4, column=1, sticky="ew", padx=10, pady=8)
    curso_combobox.set("")  # Inicia vazio

    # Configurar pesos da grid
    main_frame.grid_columnconfigure(1, weight=1)

    # Frame dos botões
    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=5, column=0, columnspan=2, pady=25)

    def adicionar_aluno():
        nome = nome_entry.get().strip()
        ra = ra_entry.get().strip()
        turma = turma_combobox.get().strip()
        curso = curso_combobox.get().strip()

        if not nome or not ra or not turma or not curso:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        # Verificar se RA já existe
        alunos = carregar_alunos()
        ra_existente = any(aluno.get("RA", "").strip().lower() == ra.strip().lower() for aluno in alunos)
        if ra_existente:
            messagebox.showwarning("RA duplicado", "Já existe um aluno cadastrado com este RA!")
            return

        alunos.append({
            "nome": nome,
            "RA": ra,
            "turma": turma,
            "curso": curso,
            "email": ra  # Usa o RA como email também
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

    btn_add_aluno = criar_botao_hover(btn_frame, "Adicionar Aluno", "#4CAF50", adicionar_aluno)
    btn_add_aluno.pack(side="left", padx=10)

    btn_voltar = criar_botao_hover(btn_frame, "Voltar ao Menu", "#3498db", voltar_menu)
    btn_voltar.pack(side="left", padx=10)

    # Enter aciona o botão
    nome_entry.bind("<Return>", lambda event: adicionar_aluno())
    ra_entry.bind("<Return>", lambda event: adicionar_aluno())
    turma_combobox.bind("<Return>", lambda event: adicionar_aluno())
    curso_combobox.bind("<Return>", lambda event: adicionar_aluno())

    # Focar no primeiro campo
    nome_entry.focus_set()

# ===================== TELA DE(TURMAS) COM FILTRO =====================
def listar_disciplinas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    disciplinas = carregar_disciplinas()
    
    # Criar janela com filtro
    lista_janela = tk.Toplevel()
    lista_janela.title("Turmas Cadastradas")
    lista_janela.geometry("1000x600")
    lista_janela.configure(bg="#d9d9d9")

    # Frame do título e filtro
    header_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    header_frame.pack(fill="x", pady=10, padx=20)
    
    tk.Label(header_frame, text="Turmas Cadastradas", bg="#d9d9d9",
             font=("Arial", 14, "bold")).pack(side="left")

    # Frame do filtro (lado direito)
    filter_frame = tk.Frame(header_frame, bg="#d9d9d9")
    filter_frame.pack(side="right")
    
    tk.Label(filter_frame, text="Filtrar por Matéria:", bg="#d9d9d9", 
             font=("Arial", 10)).pack(side="left", padx=(20, 5))
    
    # Combobox para filtro de matéria
    materias_opcoes = ["Todas as Matérias"] + sorted(list({disc.get('nome', '') for disc in disciplinas if disc.get('nome')}))
    materia_filter_var = tk.StringVar(value="Todas as Matérias")
    materia_filter = ttk.Combobox(filter_frame, textvariable=materia_filter_var, 
                                 values=materias_opcoes, width=20, state="readonly")
    materia_filter.pack(side="left", padx=5)
    
    # Label contador
    contador_label = tk.Label(header_frame, text=f"Total de turmas: {len(disciplinas)}", 
                             bg="#d9d9d9", font=("Arial", 10))
    contador_label.pack(side="left", padx=20)

    # Frame da tabela
    frame_tabela = tk.Frame(lista_janela, bg="#d9d9d9")
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    if not disciplinas:
        tk.Label(frame_tabela, text="Nenhuma turma cadastrada.",
                 bg="#d9d9d9", font=("Arial", 11)).pack()
        tree = None
    else:
        # Criar Treeview
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
                  foreground=[("selected", "#000000")])

        tree = ttk.Treeview(frame_tabela, columns=["Matéria", "Código", "Professor", "Turma", "Curso", "Carga Horária"], 
                           show="headings", height=15)
        
        # Definir headings
        tree.heading("Matéria", text="Matéria")
        tree.heading("Código", text="Código")
        tree.heading("Professor", text="Professor")
        tree.heading("Turma", text="Turma")
        tree.heading("Curso", text="Curso")
        tree.heading("Carga Horária", text="Carga Horária")
        
        # Definir larguras
        tree.column("Matéria", width=180, anchor="center")
        tree.column("Código", width=80, anchor="center")
        tree.column("Professor", width=100, anchor="center")
        tree.column("Turma", width=80, anchor="center")
        tree.column("Curso", width=120, anchor="center")
        tree.column("Carga Horária", width=100, anchor="center")
        
        # Adicionar scrollbars
        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Inserir dados iniciais
        for disc in disciplinas:
            tree.insert("", "end", values=(
                disc.get('nome', '-'),
                disc.get('codigo', '-'),
                disc.get('professor', '-'),
                disc.get('turma', '-'),
                disc.get('curso', '-'),
                f"{disc.get('carga_horaria', '-')}h"
            ))
        
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

    # Função para aplicar filtro
    def aplicar_filtro():
        materia_selecionada = materia_filter_var.get()
        if materia_selecionada == "Todas as Matérias":
            disciplinas_filtradas = disciplinas
        else:
            disciplinas_filtradas = [disc for disc in disciplinas if disc.get('nome') == materia_selecionada]
        
        # Atualizar a tabela
        for item in tree.get_children():
            tree.delete(item)
            
        for disc in disciplinas_filtradas:
            tree.insert("", "end", values=(
                disc.get('nome', '-'),
                disc.get('codigo', '-'),
                disc.get('professor', '-'),
                disc.get('turma', '-'),
                disc.get('curso', '-'),
                f"{disc.get('carga_horaria', '-')}h"
            ))
        
        # Atualizar contador
        contador_label.config(text=f"Total de turmas: {len(disciplinas_filtradas)}")

    # Botão Voltar ao Menu
    btn_voltar_menu = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=voltar_menu)
    btn_voltar_menu.pack(side="left", padx=5)

    # Botão Remover Selecionado (apenas se houver dados)
    if disciplinas and tree:
        def remover_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione uma turma para remover.")
                return
            
            confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja remover a turma selecionada?")
            if not confirmacao:
                return
            
            try:
                item_selecionado = selecionado[0]
                valores = tree.item(item_selecionado, 'values')
                remover_disciplina(valores)
                
                tree.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Turma removida com sucesso!")
                
                # Atualizar contador
                materia_atual = materia_filter_var.get()
                if materia_atual == "Todas as Matérias":
                    disciplinas_restantes = carregar_disciplinas()
                else:
                    disciplinas_restantes = [disc for disc in carregar_disciplinas() if disc.get('nome') == materia_atual]
                contador_label.config(text=f"Total de turmas: {len(disciplinas_restantes)}")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover turma: {str(e)}")

        btn_remover = tk.Button(btn_frame, text="Remover Selecionado", bg="#e74c3c", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=remover_selecionado)
        btn_remover.pack(side="left", padx=5)

    # Botão Adicionar Nova Turma
    btn_adicionar = tk.Button(btn_frame, text="Adicionar Nova Turma", bg="#4CAF50", fg="white",
                            font=("Arial", 10, "bold"), relief="raised", 
                            command=lambda: [lista_janela.destroy(), abrir_tela_disciplinas(parent_window)])
    btn_adicionar.pack(side="left", padx=5)
    
    # Botão Limpar Filtro
    def limpar_filtro():
        materia_filter_var.set("Todas as Matérias")
        aplicar_filtro()

    btn_limpar = tk.Button(btn_frame, text="Limpar Filtro", bg="#f39c12", fg="white",
                          font=("Arial", 10, "bold"), relief="raised", 
                          command=limpar_filtro)
    btn_limpar.pack(side="left", padx=5)

    # Aplicar filtro automaticamente quando selecionar uma matéria
    materia_filter.bind('<<ComboboxSelected>>', lambda event: aplicar_filtro())

    return lista_janela

# ===================== TELA DE CADASTRO DE TURMAS =====================
def abrir_tela_disciplinas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Turma")
    janela_cadastro.geometry("500x550")
    janela_cadastro.config(bg="#dcdcdc")
    janela_cadastro.resizable(False, False)

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Turma", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Matéria:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
    
    # COMBOBOX para Matéria
    disciplinas_opcoes = [
        "Engenharia de Software",
        "Programação Python", 
        "Programação C++",
        "Banco de Dados",
        "Redes de Computadores",
        "Sistemas Operacionais",
        "Estrutura de Dados",
        "Inteligência Artificial"
    ]
    nome_combobox = ttk.Combobox(main_frame, values=disciplinas_opcoes, width=25, font=("Arial", 10))
    nome_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=8)
    nome_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Código:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
    
    # COMBOBOX para Código
    codigos_opcoes = ["ENG001", "PYT002", "CPP003", "BD004", "RED005", "SO006", "ED007", "IA008"]
    codigo_combobox = ttk.Combobox(main_frame, values=codigos_opcoes, width=25, font=("Arial", 10))
    codigo_combobox.grid(row=2, column=1, sticky="ew", padx=10, pady=8)
    codigo_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Professor:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
    
    # COMBOBOX para Professor com nomes pré-definidos
    professores_opcoes = ["Aldy", "Raul", "Rogerio"]
    professor_combobox = ttk.Combobox(main_frame, values=professores_opcoes, width=25, font=("Arial", 10))
    professor_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=8)
    professor_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Turma:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=8)
    
    # COMBOBOX para Turma com opções pré-definidas
    turmas_opcoes = ["ADS1", "ADS2", "ADS3", "ADS4", "ADS5", "ADS6"]
    turma_combobox = ttk.Combobox(main_frame, values=turmas_opcoes, width=25, font=("Arial", 10))
    turma_combobox.grid(row=4, column=1, sticky="ew", padx=10, pady=8)
    turma_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Curso:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="w", pady=8)
    
    # COMBOBOX para Curso com opções pré-definidas
    cursos_opcoes = [
        "ADS - Análise e Desenvolvimento de Sistemas",
        "GTI - Gestão da Tecnologia da Informação", 
        "SI - Sistemas de Informação",
        "CC - Ciência da Computação",
        "EC - Engenharia da Computação",
        "RC - Redes de Computadores"
    ]
    curso_combobox = ttk.Combobox(main_frame, values=cursos_opcoes, width=25, font=("Arial", 10))
    curso_combobox.grid(row=5, column=1, sticky="ew", padx=10, pady=8)
    curso_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Carga Horária (h):", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w", pady=8)
    
    # COMBOBOX para Carga Horária
    carga_opcoes = ["40", "60", "80", "100", "120"]
    carga_combobox = ttk.Combobox(main_frame, values=carga_opcoes, width=25, font=("Arial", 10))
    carga_combobox.grid(row=6, column=1, sticky="ew", padx=10, pady=8)
    carga_combobox.set("")  # Inicia vazio

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=7, column=0, columnspan=2, pady=25)

    def adicionar_disciplina():
        nome = nome_combobox.get().strip()
        codigo = codigo_combobox.get().strip()
        professor = professor_combobox.get().strip()
        turma = turma_combobox.get().strip()
        curso = curso_combobox.get().strip()
        carga = carga_combobox.get().strip()

        if not nome or not codigo or not professor or not turma or not curso or not carga:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        # Verificar se código já existe
        disciplinas = carregar_disciplinas()
        codigo_existente = any(disc.get("codigo", "").strip().lower() == codigo.strip().lower() for disc in disciplinas)
        if codigo_existente:
            messagebox.showwarning("Código duplicado", "Já existe uma turma cadastrada com este código!")
            return

        disciplinas.append({
            "nome": nome,
            "codigo": codigo,
            "professor": professor,
            "turma": turma,
            "curso": curso,
            "carga_horaria": carga
        })
        salvar_disciplinas(disciplinas)

        messagebox.showinfo("Sucesso", "Turma cadastrada com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()
            listar_disciplinas(parent_window)

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

    btn_add_disciplina = criar_botao_hover(btn_frame, "Adicionar Turma", "#4CAF50", adicionar_disciplina)
    btn_add_disciplina.pack(side="left", padx=10)

    btn_voltar = criar_botao_hover(btn_frame, "Voltar ao Menu", "#3498db", voltar_menu)
    btn_voltar.pack(side="left", padx=10)

    # Bind Enter para todos os campos
    nome_combobox.bind("<Return>", lambda event: adicionar_disciplina())
    codigo_combobox.bind("<Return>", lambda event: adicionar_disciplina())
    professor_combobox.bind("<Return>", lambda event: adicionar_disciplina())
    turma_combobox.bind("<Return>", lambda event: adicionar_disciplina())
    curso_combobox.bind("<Return>", lambda event: adicionar_disciplina())
    carga_combobox.bind("<Return>", lambda event: adicionar_disciplina())

    # Focar no primeiro campo
    nome_combobox.focus_set()

# ===================== TELA DE NOTAS COM FILTRO POR DISCIPLINA =====================
def listar_notas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    notas = carregar_notas()
    
    # Criar janela com filtro
    lista_janela = tk.Toplevel()
    lista_janela.title("Notas Cadastradas")
    lista_janela.geometry("1100x600")
    lista_janela.configure(bg="#d9d9d9")

    # Frame do título e filtro
    header_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    header_frame.pack(fill="x", pady=10, padx=20)
    
    tk.Label(header_frame, text="Notas Cadastradas", bg="#d9d9d9",
             font=("Arial", 14, "bold")).pack(side="left")

    # Frame do filtro (lado direito)
    filter_frame = tk.Frame(header_frame, bg="#d9d9d9")
    filter_frame.pack(side="right")
    
    tk.Label(filter_frame, text="Filtrar por Disciplina:", bg="#d9d9d9", 
             font=("Arial", 10)).pack(side="left", padx=(20, 5))
    
    # Combobox para filtro de disciplina
    disciplinas_opcoes = ["Todas as Disciplinas"] + sorted(list({nota.get('disciplina', '') for nota in notas if nota.get('disciplina')}))
    disciplina_filter_var = tk.StringVar(value="Todas as Disciplinas")
    disciplina_filter = ttk.Combobox(filter_frame, textvariable=disciplina_filter_var, 
                                   values=disciplinas_opcoes, width=20, state="readonly")
    disciplina_filter.pack(side="left", padx=5)
    
    # Label contador
    contador_label = tk.Label(header_frame, text=f"Total de registros: {len(notas)}", 
                             bg="#d9d9d9", font=("Arial", 10))
    contador_label.pack(side="left", padx=20)

    # Frame da tabela
    frame_tabela = tk.Frame(lista_janela, bg="#d9d9d9")
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    if not notas:
        tk.Label(frame_tabela, text="Nenhuma nota cadastrada.",
                 bg="#d9d9d9", font=("Arial", 11)).pack()
        tree = None
    else:
        # Criar Treeview
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
                  foreground=[("selected", "#000000")])

        tree = ttk.Treeview(frame_tabela, columns=["Aluno", "Turma", "Disciplina", "NP1", "NP2", "Média"], 
                           show="headings", height=15)
        
        # Definir headings
        tree.heading("Aluno", text="Aluno")
        tree.heading("Turma", text="Turma")
        tree.heading("Disciplina", text="Disciplina")
        tree.heading("NP1", text="NP1")
        tree.heading("NP2", text="NP2")
        tree.heading("Média", text="Média")
        
        # Definir larguras
        tree.column("Aluno", width=200, anchor="center")
        tree.column("Turma", width=100, anchor="center")
        tree.column("Disciplina", width=150, anchor="center")
        tree.column("NP1", width=80, anchor="center")
        tree.column("NP2", width=80, anchor="center")
        tree.column("Média", width=80, anchor="center")
        
        # Adicionar scrollbars
        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # CORREÇÃO: Inserir dados iniciais CORRETAMENTE
        for nota in notas:
            # Calcular média
            np1 = nota.get('np1', '-')
            np2 = nota.get('np2', '-')
            
            if np1 != '-' and np2 != '-':
                try:
                    np1_float = float(np1)
                    np2_float = float(np2)
                    media = (np1_float + np2_float) / 2
                    media_str = f"{media:.1f}"
                except:
                    media_str = "-"
            else:
                media_str = "-"
            
            tree.insert("", "end", values=(
                nota.get('aluno', '-'),
                nota.get('turma', '-'),
                nota.get('disciplina', '-'),
                np1,
                np2,
                media_str
            ))
        
        # Posicionar elementos
        tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Configurar grid weights
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Função para editar nota
        def editar_nota():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um registro para editar.")
                return
            
            item = selecionado[0]
            valores = tree.item(item, 'values')
            
            # Criar janela de edição
            editar_janela = tk.Toplevel(lista_janela)
            editar_janela.title("Editar Notas")
            editar_janela.geometry("400x300")
            editar_janela.configure(bg="#dcdcdc")
            editar_janela.resizable(False, False)
            editar_janela.transient(lista_janela)
            editar_janela.grab_set()
            
            # Centralizar janela
            editar_janela.update_idletasks()
            x = (editar_janela.winfo_screenwidth() // 2) - (editar_janela.winfo_width() // 2)
            y = (editar_janela.winfo_screenheight() // 2) - (editar_janela.winfo_height() // 2)
            editar_janela.geometry(f"+{x}+{y}")
            
            # Frame principal
            main_frame = tk.Frame(editar_janela, bg="#dcdcdc")
            main_frame.pack(fill="both", expand=True, padx=20, pady=20)
            
            tk.Label(main_frame, text=f"Editar notas de {valores[0]}", 
                    bg="#dcdcdc", font=("Arial", 14, "bold")).pack(pady=(0, 10))
            
            tk.Label(main_frame, text=f"Disciplina: {valores[2]} | Turma: {valores[1]}", 
                    bg="#dcdcdc", font=("Arial", 11)).pack(pady=5)
            
            # Frame para NP1
            np1_frame = tk.Frame(main_frame, bg="#dcdcdc")
            np1_frame.pack(fill="x", pady=10)
            
            tk.Label(np1_frame, text="NP1:", bg="#dcdcdc", 
                    font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))
            
            notas_opcoes = ["-", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0"]
            np1_var = tk.StringVar(value=valores[3])
            np1_combobox = ttk.Combobox(np1_frame, textvariable=np1_var,
                                       values=notas_opcoes, width=10, state="readonly")
            np1_combobox.pack(side="left")
            
            # Frame para NP2
            np2_frame = tk.Frame(main_frame, bg="#dcdcdc")
            np2_frame.pack(fill="x", pady=10)
            
            tk.Label(np2_frame, text="NP2:", bg="#dcdcdc", 
                    font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))
            
            np2_var = tk.StringVar(value=valores[4])
            np2_combobox = ttk.Combobox(np2_frame, textvariable=np2_var,
                                       values=notas_opcoes, width=10, state="readonly")
            np2_combobox.pack(side="left")
            
            # Label para mostrar a média calculada
            media_atual = valores[5]
            media_label = tk.Label(main_frame, text=f"Média Atual: {media_atual}", 
                                  bg="#dcdcdc", font=("Arial", 11, "bold"),
                                  fg="#27ae60" if media_atual != "-" and float(media_atual) >= 6.0 else "#e74c3c")
            media_label.pack(pady=10)
            
            # Função para calcular média em tempo real
            def calcular_media():
                np1_val = np1_var.get()
                np2_val = np2_var.get()
                
                if np1_val != "-" and np2_val != "-":
                    try:
                        nova_media = (float(np1_val) + float(np2_val)) / 2
                        media_label.config(text=f"Média: {nova_media:.1f}")
                        
                        # Colorir conforme a média
                        if nova_media >= 6.0:
                            media_label.config(fg="#27ae60")  # Verde para aprovado
                        else:
                            media_label.config(fg="#e74c3c")  # Vermelho para reprovado
                    except ValueError:
                        media_label.config(text="Média: --", fg="#2c3e50")
                else:
                    media_label.config(text="Média: --", fg="#2c3e50")
            
            # Vincular o cálculo da média às comboboxes
            np1_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())
            np2_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())
            
            # Frame dos botões
            btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
            btn_frame.pack(pady=20)
            
            def salvar_edicao():
                np1 = np1_var.get().strip()
                np2 = np2_var.get().strip()
                
                if not np1 or not np2:
                    messagebox.showwarning("Aviso", "Preencha ambas as notas!")
                    return
                
                # Atualizar nos dados
                notas_atualizadas = carregar_notas()
                for nota in notas_atualizadas:
                    if (nota.get('aluno') == valores[0] and 
                        nota.get('turma') == valores[1] and 
                        nota.get('disciplina') == valores[2]):
                        
                        nota['np1'] = np1
                        nota['np2'] = np2
                        break
                
                salvar_notas(notas_atualizadas)
                
                # Recalcular média
                if np1 != "-" and np2 != "-":
                    nova_media = (float(np1) + float(np2)) / 2
                    nova_media_str = f"{nova_media:.1f}"
                else:
                    nova_media_str = "-"
                
                # Atualizar na tabela
                novos_valores = (
                    valores[0],  # Aluno
                    valores[1],  # Turma
                    valores[2],  # Disciplina
                    np1,         # NP1
                    np2,         # NP2
                    nova_media_str  # Média
                )
                
                tree.item(item, values=novos_valores)
                
                messagebox.showinfo("Sucesso", "Notas atualizadas com sucesso!")
                editar_janela.destroy()
            
            def cancelar_edicao():
                editar_janela.destroy()
            
            btn_salvar = tk.Button(btn_frame, text="Salvar", bg="#4CAF50", fg="white",
                                 font=("Arial", 10, "bold"), width=12,
                                 command=salvar_edicao)
            btn_salvar.pack(side="left", padx=5)
            
            btn_cancelar = tk.Button(btn_frame, text="Cancelar", bg="#e74c3c", fg="white",
                                   font=("Arial", 10, "bold"), width=12,
                                   command=cancelar_edicao)
            btn_cancelar.pack(side="left", padx=5)
            
            # Focar no primeiro combobox
            np1_combobox.focus_set()
            
            # Calcular média inicial
            calcular_media()

    # Frame dos botões
    btn_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    btn_frame.pack(pady=10)

    # Função para voltar ao menu
    def voltar_menu():
        lista_janela.destroy()
        if parent_window:
            parent_window.deiconify()

    # Função para aplicar filtro
    def aplicar_filtro():
        disciplina_selecionada = disciplina_filter_var.get()
        if disciplina_selecionada == "Todas as Disciplinas":
            notas_filtradas = notas
        else:
            notas_filtradas = [nota for nota in notas if nota.get('disciplina') == disciplina_selecionada]
        
        # Atualizar a tabela
        for item in tree.get_children():
            tree.delete(item)
            
        for nota in notas_filtradas:
            # Calcular média
            np1 = nota.get('np1', '-')
            np2 = nota.get('np2', '-')
            
            if np1 != '-' and np2 != '-':
                try:
                    np1_float = float(np1)
                    np2_float = float(np2)
                    media = (np1_float + np2_float) / 2
                    media_str = f"{media:.1f}"
                except:
                    media_str = "-"
            else:
                media_str = "-"
            
            tree.insert("", "end", values=(
                nota.get('aluno', '-'),
                nota.get('turma', '-'),
                nota.get('disciplina', '-'),
                np1,
                np2,
                media_str
            ))
        
        # Atualizar contador
        contador_label.config(text=f"Total de registros: {len(notas_filtradas)}")

    # Botão Voltar ao Menu
    btn_voltar_menu = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=voltar_menu)
    btn_voltar_menu.pack(side="left", padx=5)

    # Botão Editar Selecionado (apenas se houver dados)
    if notas and tree:
        btn_editar = tk.Button(btn_frame, text="Editar Selecionado", bg="#f39c12", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=editar_nota)
        btn_editar.pack(side="left", padx=5)

    # Botão Remover Selecionado (apenas se houver dados)
    if notas and tree:
        def remover_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um registro para remover.")
                return
            
            confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja remover o registro selecionado?")
            if not confirmacao:
                return
            
            try:
                item_selecionado = selecionado[0]
                valores = tree.item(item_selecionado, 'values')
                remover_nota(valores)
                
                tree.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Registro removido com sucesso!")
                
                # Atualizar contador
                disciplina_atual = disciplina_filter_var.get()
                if disciplina_atual == "Todas as Disciplinas":
                    notas_restantes = carregar_notas()
                else:
                    notas_restantes = [nota for nota in carregar_notas() if nota.get('disciplina') == disciplina_atual]
                contador_label.config(text=f"Total de registros: {len(notas_restantes)}")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover registro: {str(e)}")

        btn_remover = tk.Button(btn_frame, text="Remover Selecionado", bg="#e74c3c", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=remover_selecionado)
        btn_remover.pack(side="left", padx=5)

    # Botão Adicionar Nova Nota
    btn_adicionar = tk.Button(btn_frame, text="Adicionar Nova Nota", bg="#4CAF50", fg="white",
                            font=("Arial", 10, "bold"), relief="raised", 
                            command=lambda: [lista_janela.destroy(), abrir_tela_notas(parent_window)])
    btn_adicionar.pack(side="left", padx=5)
    
    # Botão Limpar Filtro
    def limpar_filtro():
        disciplina_filter_var.set("Todas as Disciplinas")
        aplicar_filtro()

    btn_limpar = tk.Button(btn_frame, text="Limpar Filtro", bg="#f39c12", fg="white",
                          font=("Arial", 10, "bold"), relief="raised", 
                          command=limpar_filtro)
    btn_limpar.pack(side="left", padx=5)

    # Aplicar filtro automaticamente quando selecionar uma disciplina
    if notas and tree:
        disciplina_filter.bind('<<ComboboxSelected>>', lambda event: aplicar_filtro())

    return lista_janela

# ===================== TELA DE CADASTRO DE NOTAS COM NP1 E NP2 =====================
def abrir_tela_notas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Notas")
    janela_cadastro.geometry("500x500")
    janela_cadastro.config(bg="#dcdcdc")
    janela_cadastro.resizable(False, False)

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Notas", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Formulário em grid
    tk.Label(main_frame, text="Aluno:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
    alunos = [a.get('nome') for a in carregar_alunos()]
    aluno_combobox = ttk.Combobox(main_frame, values=alunos, width=28, font=("Arial", 10))
    aluno_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=8)
    aluno_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Turma:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
    turmas = list({a.get('turma') for a in carregar_alunos()})
    turma_combobox = ttk.Combobox(main_frame, values=turmas, width=28, font=("Arial", 10))
    turma_combobox.grid(row=2, column=1, sticky="ew", padx=10, pady=8)
    turma_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="Disciplina:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
    disciplinas = [d.get('nome') for d in carregar_disciplinas()]
    disciplina_combobox = ttk.Combobox(main_frame, values=disciplinas, width=28, font=("Arial", 10))
    disciplina_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=8)
    disciplina_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="NP1:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=8)
    
    # COMBOBOX para NP1
    notas_opcoes = ["0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0"]
    np1_combobox = ttk.Combobox(main_frame, values=notas_opcoes, width=28, font=("Arial", 10))
    np1_combobox.grid(row=4, column=1, sticky="ew", padx=10, pady=8)
    np1_combobox.set("")  # Inicia vazio

    tk.Label(main_frame, text="NP2:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="w", pady=8)
    
    # COMBOBOX para NP2
    np2_combobox = ttk.Combobox(main_frame, values=notas_opcoes, width=28, font=("Arial", 10))
    np2_combobox.grid(row=5, column=1, sticky="ew", padx=10, pady=8)
    np2_combobox.set("")  # Inicia vazio

    # Label para mostrar a média calculada
    media_label = tk.Label(main_frame, text="Média: --", bg="#dcdcdc", 
                          font=("Arial", 11, "bold"), fg="#2c3e50")
    media_label.grid(row=6, column=0, columnspan=2, pady=10)

    # Função para calcular e mostrar a média
    def calcular_media():
        np1 = np1_combobox.get().strip()
        np2 = np2_combobox.get().strip()
        
        if np1 and np2:
            try:
                media = (float(np1) + float(np2)) / 2
                media_label.config(text=f"Média: {media:.1f}")
                
                # Colorir conforme a média
                if media >= 6.0:
                    media_label.config(fg="#27ae60")  # Verde para aprovado
                else:
                    media_label.config(fg="#e74c3c")  # Vermelho para reprovado
            except ValueError:
                media_label.config(text="Média: --", fg="#2c3e50")
        else:
            media_label.config(text="Média: --", fg="#2c3e50")

    # Vincular o cálculo da média às comboboxes
    np1_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())
    np2_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=7, column=0, columnspan=2, pady=25)

    def adicionar_nota():
        aluno = aluno_combobox.get().strip()
        turma = turma_combobox.get().strip()
        disciplina = disciplina_combobox.get().strip()
        np1 = np1_combobox.get().strip()
        np2 = np2_combobox.get().strip()

        if not aluno or not turma or not disciplina or not np1 or not np2:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        # Verificar se já existe nota para este aluno nesta disciplina
        notas = carregar_notas()
        nota_existente = any(
            n.get('aluno') == aluno and 
            n.get('disciplina') == disciplina 
            for n in notas
        )
        
        if nota_existente:
            messagebox.showwarning("Registro duplicado", "Já existe uma nota cadastrada para este aluno nesta disciplina!")
            return

        notas.append({
            "aluno": aluno,
            "turma": turma,
            "disciplina": disciplina,
            "np1": np1,
            "np2": np2
        })
        salvar_notas(notas)

        messagebox.showinfo("Sucesso", "Notas cadastradas com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()
            listar_notas(parent_window)

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

    btn_add_nota = criar_botao_hover(btn_frame, "Adicionar Notas", "#4CAF50", adicionar_nota)
    btn_add_nota.pack(side="left", padx=10)

    btn_voltar = criar_botao_hover(btn_frame, "Voltar ao Menu", "#3498db", voltar_menu)
    btn_voltar.pack(side="left", padx=10)

    # Bind Enter para todos os campos
    aluno_combobox.bind("<Return>", lambda event: adicionar_nota())
    turma_combobox.bind("<Return>", lambda event: adicionar_nota())
    disciplina_combobox.bind("<Return>", lambda event: adicionar_nota())
    np1_combobox.bind("<Return>", lambda event: adicionar_nota())
    np2_combobox.bind("<Return>", lambda event: adicionar_nota())

    # Focar no primeiro campo
    aluno_combobox.focus_set()

    return janela_cadastro

# ===================== TELA DE FALTAS COM FILTRO E EDIÇÃO =====================
def listar_faltas(parent_window=None):
    if parent_window:
        parent_window.withdraw()
        
    faltas = carregar_faltas()
    
    # Criar janela com filtro
    lista_janela = tk.Toplevel()
    lista_janela.title("Faltas Cadastradas")
    lista_janela.geometry("1000x600")
    lista_janela.configure(bg="#d9d9d9")

    # Frame do título e filtro
    header_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    header_frame.pack(fill="x", pady=10, padx=20)
    
    tk.Label(header_frame, text="Faltas Cadastradas", bg="#d9d9d9",
             font=("Arial", 14, "bold")).pack(side="left")

    # Frame do filtro (lado direito)
    filter_frame = tk.Frame(header_frame, bg="#d9d9d9")
    filter_frame.pack(side="right")
    
    tk.Label(filter_frame, text="Filtrar por Turma:", bg="#d9d9d9", 
             font=("Arial", 10)).pack(side="left", padx=(20, 5))
    
    # Combobox para filtro de turma
    turmas_opcoes = ["Todas as Turmas"] + sorted(list({falta.get('turma', '') for falta in faltas if falta.get('turma')}))
    turma_filter_var = tk.StringVar(value="Todas as Turmas")
    turma_filter = ttk.Combobox(filter_frame, textvariable=turma_filter_var, 
                               values=turmas_opcoes, width=15, state="readonly")
    turma_filter.pack(side="left", padx=5)
    
    # Label contador
    contador_label = tk.Label(header_frame, text=f"Total de faltas: {len(faltas)}", 
                             bg="#d9d9d9", font=("Arial", 10))
    contador_label.pack(side="left", padx=20)

    # Frame da tabela
    frame_tabela = tk.Frame(lista_janela, bg="#d9d9d9")
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    if not faltas:
        tk.Label(frame_tabela, text="Nenhuma falta cadastrada.",
                 bg="#d9d9d9", font=("Arial", 11)).pack()
        tree = None
    else:
        # Criar Treeview
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
                  foreground=[("selected", "#000000")])

        tree = ttk.Treeview(frame_tabela, columns=["Aluno", "RA", "Turma", "Disciplina", "Data", "Quantidade"], 
                           show="headings", height=15)
        
        # Definir headings
        tree.heading("Aluno", text="Aluno")
        tree.heading("RA", text="RA")
        tree.heading("Turma", text="Turma")
        tree.heading("Disciplina", text="Disciplina")
        tree.heading("Data", text="Data")
        tree.heading("Quantidade", text="Quantidade")
        
        # Definir larguras
        tree.column("Aluno", width=200, anchor="center")
        tree.column("RA", width=100, anchor="center")
        tree.column("Turma", width=80, anchor="center")
        tree.column("Disciplina", width=150, anchor="center")
        tree.column("Data", width=100, anchor="center")
        tree.column("Quantidade", width=100, anchor="center")
        
        # Adicionar scrollbars
        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Inserir dados iniciais
        for falta in faltas:
            # Obter a turma do aluno
            alunos_data = carregar_alunos()
            turma_aluno = ""
            for aluno in alunos_data:
                if aluno.get('nome') == falta.get('aluno') or aluno.get('RA') == falta.get('ra'):
                    turma_aluno = aluno.get('turma', '')
                    break
            
            tree.insert("", "end", values=(
                falta.get('aluno', '-'),
                falta.get('ra', '-'),
                turma_aluno,
                falta.get('disciplina', '-'),
                falta.get('data', '-'),
                falta.get('quantidade', '-')
            ))
        
        # Posicionar elementos
        tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Configurar grid weights
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Função para editar quantidade de faltas com duplo clique
        def editar_falta(event):
            item = tree.selection()[0] if tree.selection() else None
            if item:
                # Verificar se o clique foi na coluna da quantidade (coluna 5)
                column = tree.identify_column(event.x)
                if column == '#6':  # Coluna da quantidade (índice 5)
                    valores = tree.item(item, 'values')
                    
                    # Criar janela de edição
                    editar_janela = tk.Toplevel(lista_janela)
                    editar_janela.title("Editar Falta")
                    editar_janela.geometry("350x200")
                    editar_janela.configure(bg="#dcdcdc")
                    editar_janela.resizable(False, False)
                    editar_janela.transient(lista_janela)
                    editar_janela.grab_set()
                    
                    # Centralizar janela
                    editar_janela.update_idletasks()
                    x = (editar_janela.winfo_screenwidth() // 2) - (editar_janela.winfo_width() // 2)
                    y = (editar_janela.winfo_screenheight() // 2) - (editar_janela.winfo_height() // 2)
                    editar_janela.geometry(f"+{x}+{y}")
                    
                    # Frame principal
                    main_frame = tk.Frame(editar_janela, bg="#dcdcdc")
                    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
                    
                    tk.Label(main_frame, text=f"Editar falta de {valores[0]}", 
                            bg="#dcdcdc", font=("Arial", 12, "bold")).pack(pady=(0, 10))
                    
                    tk.Label(main_frame, text=f"Disciplina: {valores[3]} | Data: {valores[4]}", 
                            bg="#dcdcdc", font=("Arial", 10)).pack(pady=5)
                    
                    tk.Label(main_frame, text="Nova quantidade:", bg="#dcdcdc", 
                            font=("Arial", 10)).pack(pady=5)
                    
                    # Entry para nova quantidade
                    nova_quantidade_var = tk.StringVar(value=valores[5])
                    nova_quantidade_entry = ttk.Entry(main_frame, textvariable=nova_quantidade_var,
                                                     width=10, font=("Arial", 10), justify="center")
                    nova_quantidade_entry.pack(pady=5)
                    
                    # Frame dos botões
                    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
                    btn_frame.pack(pady=15)
                    
                    def salvar_edicao():
                        nova_quantidade = nova_quantidade_var.get().strip()
                        if not nova_quantidade:
                            messagebox.showwarning("Aviso", "Digite uma quantidade!")
                            return
                        
                        try:
                            qtd = int(nova_quantidade)
                            if qtd <= 0:
                                messagebox.showwarning("Quantidade inválida", "A quantidade deve ser maior que zero")
                                return
                        except ValueError:
                            messagebox.showwarning("Quantidade inválida", "Digite um número válido para a quantidade")
                            return
                        
                        # Atualizar nos dados
                        faltas_atualizadas = carregar_faltas()
                        for falta in faltas_atualizadas:
                            if (falta.get('aluno') == valores[0] and 
                                falta.get('ra') == valores[1] and 
                                falta.get('disciplina') == valores[3] and 
                                falta.get('data') == valores[4] and 
                                falta.get('quantidade') == valores[5]):
                                falta['quantidade'] = nova_quantidade
                                break
                        
                        salvar_faltas(faltas_atualizadas)
                        
                        # Atualizar na tabela
                        tree.item(item, values=(
                            valores[0],
                            valores[1],
                            valores[2],
                            valores[3],
                            valores[4],
                            nova_quantidade
                        ))
                        
                        messagebox.showinfo("Sucesso", "Falta atualizada com sucesso!")
                        editar_janela.destroy()
                    
                    def cancelar_edicao():
                        editar_janela.destroy()
                    
                    btn_salvar = tk.Button(btn_frame, text="Salvar", bg="#4CAF50", fg="white",
                                         font=("Arial", 10, "bold"), width=10,
                                         command=salvar_edicao)
                    btn_salvar.pack(side="left", padx=5)
                    
                    btn_cancelar = tk.Button(btn_frame, text="Cancelar", bg="#e74c3c", fg="white",
                                           font=("Arial", 10, "bold"), width=10,
                                           command=cancelar_edicao)
                    btn_cancelar.pack(side="left", padx=5)
                    
                    # Focar no entry e selecionar todo o texto
                    nova_quantidade_entry.focus_set()
                    nova_quantidade_entry.select_range(0, tk.END)
                    
                    # Enter para salvar
                    nova_quantidade_entry.bind("<Return>", lambda e: salvar_edicao())

        # Vincular duplo clique à função de edição
        tree.bind("<Double-1>", editar_falta)

    # Frame dos botões
    btn_frame = tk.Frame(lista_janela, bg="#d9d9d9")
    btn_frame.pack(pady=10)

    # Função para voltar ao menu
    def voltar_menu():
        lista_janela.destroy()
        if parent_window:
            parent_window.deiconify()

    # Função para aplicar filtro
    def aplicar_filtro():
        turma_selecionada = turma_filter_var.get()
        if turma_selecionada == "Todas as Turmas":
            faltas_filtradas = faltas
        else:
            # Filtrar faltas pela turma do aluno
            alunos_data = carregar_alunos()
            alunos_da_turma = [aluno.get('nome') for aluno in alunos_data if aluno.get('turma') == turma_selecionada]
            faltas_filtradas = [falta for falta in faltas if falta.get('aluno') in alunos_da_turma]
        
        # Atualizar a tabela
        for item in tree.get_children():
            tree.delete(item)
            
        for falta in faltas_filtradas:
            # Obter a turma do aluno
            alunos_data = carregar_alunos()
            turma_aluno = ""
            for aluno in alunos_data:
                if aluno.get('nome') == falta.get('aluno') or aluno.get('RA') == falta.get('ra'):
                    turma_aluno = aluno.get('turma', '')
                    break
            
            tree.insert("", "end", values=(
                falta.get('aluno', '-'),
                falta.get('ra', '-'),
                turma_aluno,
                falta.get('disciplina', '-'),
                falta.get('data', '-'),
                falta.get('quantidade', '-')
            ))
        
        # Atualizar contador
        contador_label.config(text=f"Total de faltas: {len(faltas_filtradas)}")

    # Botão Voltar ao Menu
    btn_voltar_menu = tk.Button(btn_frame, text="Voltar ao Menu", bg="#3498db", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=voltar_menu)
    btn_voltar_menu.pack(side="left", padx=5)

    # Botão Remover Selecionado (apenas se houver dados)
    if faltas and tree:
        def remover_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione uma falta para remover.")
                return
            
            confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja remover a falta selecionada?")
            if not confirmacao:
                return
            
            try:
                item_selecionado = selecionado[0]
                valores = tree.item(item_selecionado, 'values')
                remover_falta(valores)
                
                tree.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Falta removida com sucesso!")
                
                # Atualizar contador
                turma_atual = turma_filter_var.get()
                if turma_atual == "Todas as Turmas":
                    faltas_restantes = carregar_faltas()
                else:
                    alunos_data = carregar_alunos()
                    alunos_da_turma = [aluno.get('nome') for aluno in alunos_data if aluno.get('turma') == turma_atual]
                    faltas_restantes = [falta for falta in carregar_faltas() if falta.get('aluno') in alunos_da_turma]
                contador_label.config(text=f"Total de faltas: {len(faltas_restantes)}")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover falta: {str(e)}")

        btn_remover = tk.Button(btn_frame, text="Remover Selecionado", bg="#e74c3c", fg="white",
                              font=("Arial", 10, "bold"), relief="raised", 
                              command=remover_selecionado)
        btn_remover.pack(side="left", padx=5)

    # Botão Adicionar Nova Falta
    btn_adicionar = tk.Button(btn_frame, text="Adicionar Nova Falta", bg="#4CAF50", fg="white",
                            font=("Arial", 10, "bold"), relief="raised", 
                            command=lambda: [lista_janela.destroy(), abrir_tela_faltas(parent_window)])
    btn_adicionar.pack(side="left", padx=5)
    
    # Botão Limpar Filtro
    def limpar_filtro():
        turma_filter_var.set("Todas as Turmas")
        aplicar_filtro()

    btn_limpar = tk.Button(btn_frame, text="Limpar Filtro", bg="#f39c12", fg="white",
                          font=("Arial", 10, "bold"), relief="raised", 
                          command=limpar_filtro)
    btn_limpar.pack(side="left", padx=5)

    # Aplicar filtro automaticamente quando selecionar uma turma
    turma_filter.bind('<<ComboboxSelected>>', lambda event: aplicar_filtro())

    return lista_janela

# ===================== TELA DE CADASTRO DE FALTAS =====================
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
    icone_conteudos = r"PROJETO_TKINTER\conteudos.png"
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

    # Criando botões do menu - INCLUINDO O NOVO BOTÃO DE CONTEÚDOS
    btn_aluno = criar_botao_menu("#1abc9c", "Alunos", icone_aluno, lambda: listar_alunos(tela_admin))
    btn_turmas = criar_botao_menu("#2ecc71", "Turmas", icone_disciplina, lambda: listar_disciplinas(tela_admin))
    btn_notas = criar_botao_menu("#3498db", "Notas", icone_notas, lambda: listar_notas(tela_admin))
    btn_faltas = criar_botao_menu("#e67e22", "Faltas", icone_faltas, lambda: listar_faltas(tela_admin))
    btn_conteudos = criar_botao_menu("#9b59b6", "Conteúdos", icone_conteudos, lambda: listar_conteudos(tela_admin))
    btn_config = criar_botao_menu("#34495e", "Configurações", icone_config, abrir_configuracoes)

    # Posicionando os botões em grid 3x2
    btn_aluno.grid(row=0, column=0, padx=5, pady=5)
    btn_turmas.grid(row=0, column=1, padx=5, pady=5)
    btn_notas.grid(row=1, column=0, padx=5, pady=5)
    btn_faltas.grid(row=1, column=1, padx=5, pady=5)
    btn_conteudos.grid(row=2, column=0, padx=5, pady=5)
    btn_config.grid(row=2, column=1, padx=5, pady=5)

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
    tela_aluno.title("Portal do Aluno")
    tela_aluno.geometry("1000x700")
    tela_aluno.configure(bg="#ecf0f1")

    # ===================== FUNÇÃO SAIR =====================
    def confirmar_sair():
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair e voltar ao login?")
        if resposta:
            tela_aluno.destroy()

    # ===================== CARREGAR DADOS =====================
    notas = carregar_notas()
    disciplinas = carregar_disciplinas()
    alunos = carregar_alunos()
    faltas = carregar_faltas()
    conteudos = carregar_conteudos()

    # ===================== IDENTIFICAR ALUNO =====================
    nome_aluno = None
    turma_aluno = None
    ra_aluno = None
    curso_aluno = None
    
    for a in alunos:
        if a.get("RA", "").strip().lower() == email_usuario.strip().lower() or \
           a.get("email", "").strip().lower() == email_usuario.strip().lower():
            nome_aluno = a.get("nome")
            turma_aluno = a.get("turma")
            ra_aluno = a.get("RA")
            curso_aluno = a.get("curso")
            break

    if not nome_aluno:
        messagebox.showerror("Erro", "Aluno não encontrado!")
        tela_aluno.destroy()
        return

    # ===================== CABEÇALHO =====================
    header = tk.Frame(tela_aluno, bg="#2c3e50", height=70)  # Altura ajustada
    header.pack(fill="x", pady=10, padx=20)
    header.pack_propagate(False)  # IMPEDE QUE O FRAME REDUZA DE TAMANHO

    # Informações do aluno
    info_frame = tk.Frame(header, bg="#2c3e50")
    info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=12)
    
    tk.Label(info_frame, text=f"Bem-vindo(a), {nome_aluno}", 
             bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).pack(anchor="w")
    
    tk.Label(info_frame, text=f"RA: {ra_aluno} | Turma: {turma_aluno} | Curso: {curso_aluno}", 
             bg="#2c3e50", fg="#bdc3c7", font=("Arial", 11)).pack(anchor="w")

    user_icon_path = r"PROJETO_TKINTER\user.png"
    try:
        user_img = Image.open(user_icon_path).resize((25, 25), Image.Resampling.LANCZOS)  # Ícone menor
        user_icon = ImageTk.PhotoImage(user_img)
    except:
        user_icon = None

    # BOTÃO SAIR COM BORDER RADIUS - usando Frame para simular bordas arredondadas
    btn_frame = tk.Frame(header, bg="#2c3e50")
    btn_frame.pack(side="right", padx=10, pady=10)
    
    # Frame para simular bordas arredondadas
    rounded_frame = tk.Frame(btn_frame, bg="#e74c3c", relief="flat", bd=0)
    rounded_frame.pack(padx=0, pady=0)
    
    # Botão dentro do frame arredondado
    btn_logout = tk.Button(rounded_frame, text=" Sair", image=user_icon, compound="left",
                           bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                           command=confirmar_sair, relief="flat", 
                           width=15, height=10, cursor="hand2", bd=0,
                           highlightthickness=0)  # Remove a borda de foco
    btn_logout.image = user_icon
    btn_logout.pack(padx=10, pady=5)  # Padding interno para o botão
    
    # EFEITO HOVER PARA O BOTÃO SAIR
    def on_enter_sair(e):
        btn_logout.config(bg="#c0392b", font=("Arial", 10, "bold"))
        rounded_frame.config(bg="#c0392b")
    
    def on_leave_sair(e):
        btn_logout.config(bg="#e74c3c", font=("Arial", 10, "bold"))
        rounded_frame.config(bg="#e74c3c")
    
    btn_logout.bind("<Enter>", on_enter_sair)
    btn_logout.bind("<Leave>", on_leave_sair)
    rounded_frame.bind("<Enter>", on_enter_sair)
    rounded_frame.bind("<Leave>", on_leave_sair)

    # ===================== NOTEBOOK (ABAS) =====================
    notebook = ttk.Notebook(tela_aluno)
    notebook.pack(fill="both", expand=True, padx=20, pady=10)

    # ===================== ABA 1: NOTAS =====================
    frame_notas = tk.Frame(notebook, bg="#ecf0f1")
    notebook.add(frame_notas, text="📊 Notas e Médias")

    # ===================== FUNÇÃO PARA CALCULAR MÉDIA =====================
    def calcular_media(np1, np2):
        try:
            np1_float = float(np1) if np1 and np1 != '-' else 0
            np2_float = float(np2) if np2 and np2 != '-' else 0
            return (np1_float + np2_float) / 2
        except:
            return 0

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
        return total_faltas

    # ===================== MONTAR LISTA DE NOTAS DO ALUNO =====================
    disciplinas_aluno = []
    
    # Buscar todas as notas do aluno pelo RA ou nome
    for nota in notas:
        aluno_da_nota = nota.get("aluno")
        ra_da_nota = nota.get("ra", "")
        
        # Verificar se a nota pertence ao aluno atual
        if (aluno_da_nota and aluno_da_nota.strip().lower() == nome_aluno.strip().lower()) or \
           (ra_da_nota and ra_da_nota.strip().lower() == ra_aluno.strip().lower()):
            
            disciplina_nome = nota.get("disciplina", "-")
            
            # Buscar informações da disciplina
            professor = "-"
            for disc in disciplinas:
                if disc.get("nome", "").strip().lower() == disciplina_nome.strip().lower():
                    professor = disc.get("professor", "-")
                    break

            # Obter NP1 e NP2
            np1 = nota.get("np1", "-")
            np2 = nota.get("np2", "-")
            
            # Calcular média
            media = calcular_media(np1, np2)
            
            # Calcular faltas
            total_faltas = calcular_faltas_disciplina(disciplina_nome)
            
            # Determinar status
            if np1 == "-" and np2 == "-":
                status = "Cursando"
                cor_status = "#3498db"  # Azul
            elif media >= 6.0:
                status = "Aprovado"
                cor_status = "#27ae60"  # Verde
            elif media >= 4.0:
                status = "Recuperação"
                cor_status = "#f39c12"  # Laranja
            else:
                status = "Reprovado"
                cor_status = "#e74c3c"  # Vermelho

            disciplinas_aluno.append({
                "nome": disciplina_nome,
                "professor": professor,
                "np1": np1,
                "np2": np2,
                "media": f"{media:.1f}" if media > 0 else "-",
                "faltas": total_faltas,
                "status": status,
                "cor_status": cor_status
            })

    # ===================== WIDGETS DA ABA NOTAS =====================
    if not disciplinas_aluno:
        lbl_vazio = tk.Label(frame_notas, text="Nenhuma nota encontrada para este aluno.",
                             bg="#ecf0f1", fg="gray", font=("Arial", 12))
        lbl_vazio.pack(pady=50)
    else:
        # Frame de estatísticas
        stats_frame = tk.Frame(frame_notas, bg="#ecf0f1")
        stats_frame.pack(fill="x", padx=20, pady=10)
        
        # Calcular estatísticas
        total_disciplinas = len(disciplinas_aluno)
        aprovadas = sum(1 for d in disciplinas_aluno if d["status"] == "Aprovado")
        recuperacao = sum(1 for d in disciplinas_aluno if d["status"] == "Recuperação")
        reprovadas = sum(1 for d in disciplinas_aluno if d["status"] == "Reprovado")
        cursando = sum(1 for d in disciplinas_aluno if d["status"] == "Cursando")
        
        tk.Label(stats_frame, text=f"Disciplinas: {total_disciplinas} | "
                                   f"Aprovadas: {aprovadas} | "
                                   f"Recuperação: {recuperacao} | "
                                   f"Reprovadas: {reprovadas} | "
                                   f"Cursando: {cursando}",
                 bg="#ecf0f1", font=("Arial", 11, "bold")).pack()

        # Frame da tabela
        frame_tabela = tk.Frame(frame_notas, bg="#ecf0f1")
        frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

        style = ttk.Style()
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        style.configure("Treeview.Heading",
                        background="#34495e",
                        foreground="white",
                        font=("Arial", 10, "bold"))

        tree = ttk.Treeview(frame_tabela, 
                           columns=("Disciplina", "Professor", "NP1", "NP2", "Média", "Faltas", "Status"),
                           show="headings", height=15)

        tree.heading("Disciplina", text="Disciplina")
        tree.heading("Professor", text="Professor")
        tree.heading("NP1", text="NP1")
        tree.heading("NP2", text="NP2")
        tree.heading("Média", text="Média")
        tree.heading("Faltas", text="Faltas")
        tree.heading("Status", text="Status")

        tree.column("Disciplina", width=200, anchor="center")
        tree.column("Professor", width=150, anchor="center")
        tree.column("NP1", width=80, anchor="center")
        tree.column("NP2", width=80, anchor="center")
        tree.column("Média", width=80, anchor="center")
        tree.column("Faltas", width=80, anchor="center")
        tree.column("Status", width=100, anchor="center")

        v_scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Inserir dados na tabela
        for disc in disciplinas_aluno:
            tree.insert("", "end", values=(
                disc["nome"],
                disc["professor"],
                disc["np1"],
                disc["np2"],
                disc["media"],
                disc["faltas"],
                disc["status"]
            ), tags=(disc["status"],))

        # Configurar cores para os status
        tree.tag_configure("Aprovado", background="#d5f4e6")
        tree.tag_configure("Recuperação", background="#fcf3cd")
        tree.tag_configure("Reprovado", background="#fadbd8")
        tree.tag_configure("Cursando", background="#d6eaf8")

        tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Legenda de cores
        legend_frame = tk.Frame(frame_notas, bg="#ecf0f1")
        legend_frame.pack(fill="x", padx=20, pady=5)
        
        tk.Label(legend_frame, text="Legenda:", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        
        legend_colors = [
            ("Aprovado", "#d5f4e6"),
            ("Recuperação", "#fcf3cd"), 
            ("Reprovado", "#fadbd8"),
            ("Cursando", "#d6eaf8")
        ]
        
        for status, color in legend_colors:
            legend_item = tk.Frame(legend_frame, bg="#ecf0f1")
            legend_item.pack(side="left", padx=10)
            
            color_box = tk.Frame(legend_item, bg=color, width=15, height=15, relief="solid", bd=1)
            color_box.pack(side="left", padx=(0, 5))
            
            tk.Label(legend_item, text=status, bg="#ecf0f1", font=("Arial", 9)).pack(side="left")

    # ===================== ABA 2: CONTEÚDOS =====================
    frame_conteudos = tk.Frame(notebook, bg="#ecf0f1")
    notebook.add(frame_conteudos, text="📚 Conteúdos Programáticos")

    # Filtrar conteúdos pela turma do aluno
    conteudos_aluno = []
    for conteudo in conteudos:
        # Verificar se o conteúdo é da turma do aluno
        disciplina_conteudo = conteudo.get("disciplina", "")
        
        # Buscar a disciplina para verificar a turma
        for disc in disciplinas:
            if disc.get("nome", "") == disciplina_conteudo and disc.get("turma", "") == turma_aluno:
                conteudos_aluno.append(conteudo)
                break

    if not conteudos_aluno:
        lbl_vazio = tk.Label(frame_conteudos, text="Nenhum conteúdo disponível para sua turma.",
                             bg="#ecf0f1", fg="gray", font=("Arial", 12))
        lbl_vazio.pack(pady=50)
    else:
        # Frame da tabela de conteúdos
        frame_tabela_conteudos = tk.Frame(frame_conteudos, bg="#ecf0f1")
        frame_tabela_conteudos.pack(fill="both", expand=True, padx=20, pady=10)

        tree_conteudos = ttk.Treeview(frame_tabela_conteudos, 
                                     columns=("Disciplina", "Título", "Tipo", "Data", "Arquivo"),
                                     show="headings", height=15)

        tree_conteudos.heading("Disciplina", text="Disciplina")
        tree_conteudos.heading("Título", text="Título")
        tree_conteudos.heading("Tipo", text="Tipo")
        tree_conteudos.heading("Data", text="Data")
        tree_conteudos.heading("Arquivo", text="Arquivo")

        tree_conteudos.column("Disciplina", width=150, anchor="center")
        tree_conteudos.column("Título", width=200, anchor="center")
        tree_conteudos.column("Tipo", width=120, anchor="center")
        tree_conteudos.column("Data", width=100, anchor="center")
        tree_conteudos.column("Arquivo", width=150, anchor="center")

        v_scrollbar2 = ttk.Scrollbar(frame_tabela_conteudos, orient="vertical", command=tree_conteudos.yview)
        h_scrollbar2 = ttk.Scrollbar(frame_tabela_conteudos, orient="horizontal", command=tree_conteudos.xview)
        tree_conteudos.configure(yscrollcommand=v_scrollbar2.set, xscrollcommand=h_scrollbar2.set)

        for cont in conteudos_aluno:
            arquivo = "📎 Disponível" if cont.get('arquivo') and cont.get('arquivo') != '-' else "Não há"
            tree_conteudos.insert("", "end", values=(
                cont.get('disciplina', '-'),
                cont.get('titulo', '-'),
                cont.get('tipo', '-'),
                cont.get('data', '-'),
                arquivo
            ))

        tree_conteudos.grid(row=0, column=0, sticky="nsew")
        v_scrollbar2.grid(row=0, column=1, sticky="ns")
        h_scrollbar2.grid(row=1, column=0, sticky="ew")

        frame_tabela_conteudos.grid_rowconfigure(0, weight=1)
        frame_tabela_conteudos.grid_columnconfigure(0, weight=1)

        # Função para visualizar conteúdo
        def visualizar_conteudo():
            selecionado = tree_conteudos.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um conteúdo para visualizar.")
                return
            
            item = selecionado[0]
            valores = tree_conteudos.item(item, 'values')
            
            # Encontrar conteúdo completo
            conteudo_completo = None
            for cont in conteudos_aluno:
                if (cont.get('disciplina') == valores[0] and 
                    cont.get('titulo') == valores[1] and 
                    cont.get('data') == valores[3]):
                    conteudo_completo = cont
                    break
            
            if conteudo_completo:
                visualizar_janela = tk.Toplevel(tela_aluno)
                visualizar_janela.title(f"Conteúdo: {valores[1]}")
                visualizar_janela.geometry("600x500")
                visualizar_janela.configure(bg="#dcdcdc")
                
                main_frame = tk.Frame(visualizar_janela, bg="#dcdcdc")
                main_frame.pack(fill="both", expand=True, padx=20, pady=20)
                
                tk.Label(main_frame, text=conteudo_completo.get('titulo', ''), 
                        bg="#dcdcdc", font=("Arial", 16, "bold")).pack(pady=(0, 10))
                
                info_frame = tk.Frame(main_frame, bg="#dcdcdc")
                info_frame.pack(fill="x", pady=5)
                
                tk.Label(info_frame, text=f"Disciplina: {conteudo_completo.get('disciplina', '')}", 
                        bg="#dcdcdc", font=("Arial", 11)).pack(anchor="w")
                tk.Label(info_frame, text=f"Data: {conteudo_completo.get('data', '')}", 
                        bg="#dcdcdc", font=("Arial", 11)).pack(anchor="w")
                tk.Label(info_frame, text=f"Tipo: {conteudo_completo.get('tipo', '')}", 
                        bg="#dcdcdc", font=("Arial", 11)).pack(anchor="w")
                
                # Frame da descrição com scrollbar
                desc_frame = tk.Frame(main_frame, bg="#dcdcdc")
                desc_frame.pack(fill="both", expand=True, pady=10)
                
                tk.Label(desc_frame, text="Descrição:", bg="#dcdcdc", 
                        font=("Arial", 12, "bold")).pack(anchor="w")
                
                desc_text = tk.Text(desc_frame, wrap="word", width=60, height=15,
                                  font=("Arial", 10), bg="white", relief="solid", bd=1)
                desc_scrollbar = ttk.Scrollbar(desc_frame, orient="vertical", command=desc_text.yview)
                desc_text.configure(yscrollcommand=desc_scrollbar.set)
                
                desc_text.insert("1.0", conteudo_completo.get('descricao', ''))
                desc_text.config(state="disabled")
                
                desc_text.pack(side="left", fill="both", expand=True)
                desc_scrollbar.pack(side="right", fill="y")
                
                # Botão para baixar arquivo
                if conteudo_completo.get('arquivo') and conteudo_completo.get('arquivo') != '-':
                    def baixar_arquivo():
                        arquivo_path = conteudo_completo.get('arquivo')
                        if os.path.exists(arquivo_path):
                            try:
                                # Abrir o arquivo com o programa padrão
                                os.startfile(arquivo_path)
                            except:
                                messagebox.showinfo("Arquivo", f"Arquivo: {arquivo_path}")
                        else:
                            messagebox.showwarning("Arquivo não encontrado", 
                                                 "O arquivo não foi encontrado no sistema.")
                    
                    btn_baixar = tk.Button(main_frame, text="📥 Abrir Arquivo", bg="#3498db", fg="white",
                                         font=("Arial", 10, "bold"), command=baixar_arquivo)
                    btn_baixar.pack(pady=10)
                
                btn_fechar = tk.Button(main_frame, text="Fechar", bg="#e74c3c", fg="white",
                                     font=("Arial", 10, "bold"), command=visualizar_janela.destroy)
                btn_fechar.pack(pady=5)

        # Botão para visualizar conteúdo
        btn_visualizar = tk.Button(frame_conteudos, text="Visualizar Conteúdo", bg="#3498db", fg="white",
                                 font=("Arial", 10, "bold"), command=visualizar_conteudo)
        btn_visualizar.pack(pady=10)

    # ===================== ABA 3: INFORMAÇÕES PESSOAIS =====================
    frame_info = tk.Frame(notebook, bg="#ecf0f1")
    notebook.add(frame_info, text="👤 Informações Pessoais")

    # Frame das informações
    info_pessoal_frame = tk.Frame(frame_info, bg="#ecf0f1")
    info_pessoal_frame.pack(fill="both", expand=True, padx=50, pady=30)

    # Card de informações
    card_frame = tk.Frame(info_pessoal_frame, bg="white", relief="solid", bd=1)
    card_frame.pack(fill="both", expand=True)

    # Título do card
    tk.Label(card_frame, text="Dados Pessoais", bg="#34495e", fg="white",
             font=("Arial", 14, "bold"), pady=10).pack(fill="x")

    # Conteúdo do card
    content_frame = tk.Frame(card_frame, bg="white", padx=20, pady=20)
    content_frame.pack(fill="both", expand=True)

    info_labels = [
        ("Nome Completo:", nome_aluno),
        ("RA:", ra_aluno),
        ("Turma:", turma_aluno),
        ("Curso:", curso_aluno),
        ("Email:", f"{ra_aluno}@educacional.com"),
        ("Situação:", "Regular" if all(d["status"] != "Reprovado" for d in disciplinas_aluno) else "Atenção")
    ]

    for i, (label, value) in enumerate(info_labels):
        row_frame = tk.Frame(content_frame, bg="white")
        row_frame.pack(fill="x", pady=8)
        
        tk.Label(row_frame, text=label, bg="white", font=("Arial", 11, "bold"), 
                width=15, anchor="w").pack(side="left")
        tk.Label(row_frame, text=value, bg="white", font=("Arial", 11),
                width=30, anchor="w").pack(side="left")

    # Resumo acadêmico
    tk.Label(content_frame, text="Resumo Acadêmico", bg="white", 
             font=("Arial", 12, "bold"), pady=(20, 10)).pack(fill="x")

    if disciplinas_aluno:
        total_medias = sum(float(d["media"]) for d in disciplinas_aluno if d["media"] != "-")
        count_medias = sum(1 for d in disciplinas_aluno if d["media"] != "-")
        media_geral = total_medias / count_medias if count_medias > 0 else 0
        
        total_faltas = sum(d["faltas"] for d in disciplinas_aluno)
        
        resumo_info = [
            (f"Média Geral: {media_geral:.1f}", "#27ae60" if media_geral >= 6.0 else "#e74c3c"),
            (f"Total de Faltas: {total_faltas}", "#34495e"),
            (f"Disciplinas Cursadas: {len(disciplinas_aluno)}", "#3498db")
        ]
        
        for info, cor in resumo_info:
            lbl = tk.Label(content_frame, text=info, bg="white", font=("Arial", 11, "bold"),
                          fg=cor)
            lbl.pack(anchor="w", pady=2)

    # ===================== RODAPÉ =====================
    footer = tk.Frame(tela_aluno, bg="#2c3e50", height=30)
    footer.pack(fill="x", side="bottom")
    
    tk.Label(footer, text=f"© 2025 Sistema Acadêmico - {nome_aluno} ({ra_aluno})", 
             bg="#2c3e50", fg="#bdc3c7", font=("Arial", 9)).pack(pady=5)

    tela_aluno.focus_force()
    tela_aluno.lift()
    tela_aluno.mainloop()
# ===================== TELA DO PROFESSOR =====================
def abrir_tela_professor(email_professor):
    # ===================== INÍCIO DA TELA =====================
    tela_professor = tk.Tk()
    tela_professor.title("Portal do Professor")
    tela_professor.geometry("1200x800")
    tela_professor.configure(bg="#ecf0f1")

    # ===================== FUNÇÃO SAIR =====================
    def confirmar_sair():
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair e voltar ao login?")
        if resposta:
            tela_professor.destroy()

    # ===================== CARREGAR DADOS =====================
    notas = carregar_notas()
    disciplinas = carregar_disciplinas()
    alunos = carregar_alunos()
    faltas = carregar_faltas()
    conteudos = carregar_conteudos()

    # ===================== IDENTIFICAR PROFESSOR =====================
    nome_professor = None
    disciplinas_professor = []
    
    # Buscar disciplinas do professor
    for disc in disciplinas:
        if disc.get("professor", "").strip().lower() == email_professor.strip().lower():
            disciplinas_professor.append(disc)
            nome_professor = disc.get("professor")  # Usar o primeiro nome encontrado

    if not nome_professor:
        # Se não encontrou por nome, verificar se é um dos professores pré-definidos
        professores_predefinidos = ["Aldy", "Raul", "Rogerio"]
        if email_professor in professores_predefinidos:
            nome_professor = email_professor
            # Buscar todas as disciplinas deste professor
            disciplinas_professor = [disc for disc in disciplinas if disc.get("professor") == nome_professor]

    if not nome_professor:
        messagebox.showerror("Erro", "Professor não encontrado!")
        tela_professor.destroy()
        return

    # ===================== CABEÇALHO =====================
    header = tk.Frame(tela_professor, bg="#2c3e50", height=70)  # Altura ajustada
    header.pack(fill="x", pady=10, padx=20)
    header.pack_propagate(False)  # IMPEDE QUE O FRAME REDUZA DE TAMANHO

    # Informações do professor
    info_frame = tk.Frame(header, bg="#2c3e50")
    info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=12)
    
    tk.Label(info_frame, text=f"Bem-vindo(a), Prof. {nome_professor}", 
             bg="#2c3e50", fg="white", font=("Arial", 16, "bold")).pack(anchor="w")
    
    disciplinas_str = ", ".join([disc["nome"] for disc in disciplinas_professor[:3]])  # Mostrar até 3 disciplinas
    if len(disciplinas_professor) > 3:
        disciplinas_str += f" (+{len(disciplinas_professor)-3} mais)"
    
    tk.Label(info_frame, text=f"Disciplinas: {disciplinas_str}", 
             bg="#2c3e50", fg="#bdc3c7", font=("Arial", 11)).pack(anchor="w")

    user_icon_path = r"PROJETO_TKINTER\user.png"
    try:
        user_img = Image.open(user_icon_path).resize((25, 25), Image.Resampling.LANCZOS)  # Ícone menor
        user_icon = ImageTk.PhotoImage(user_img)
    except:
        user_icon = None

    # BOTÃO SAIR COM BORDER RADIUS - usando Frame para simular bordas arredondadas
    btn_frame = tk.Frame(header, bg="#2c3e50")
    btn_frame.pack(side="right", padx=15, pady=8)
    
    # Frame para simular bordas arredondadas
    rounded_frame = tk.Frame(btn_frame, bg="#e74c3c", relief="flat", bd=0)
    rounded_frame.pack(padx=0, pady=0)
    
    # Botão dentro do frame arredondado
    btn_logout = tk.Button(rounded_frame, text=" Sair", image=user_icon, compound="left",
                           bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                           command=confirmar_sair, relief="flat", 
                           width=15, height=10, cursor="hand2", bd=0,
                           highlightthickness=0)  # Remove a borda de foco
    btn_logout.image = user_icon
    btn_logout.pack(padx=8, pady=4)  # Padding interno para o botão
    
    # EFEITO HOVER PARA O BOTÃO SAIR
    def on_enter_sair(e):
        btn_logout.config(bg="#c0392b", font=("Arial", 10, "bold"))
        rounded_frame.config(bg="#c0392b")
    
    def on_leave_sair(e):
        btn_logout.config(bg="#e74c3c", font=("Arial", 10, "bold"))
        rounded_frame.config(bg="#e74c3c")
    
    btn_logout.bind("<Enter>", on_enter_sair)
    btn_logout.bind("<Leave>", on_leave_sair)
    rounded_frame.bind("<Enter>", on_enter_sair)
    rounded_frame.bind("<Leave>", on_leave_sair)

    # ===================== NOTEBOOK (ABAS) =====================
    notebook = ttk.Notebook(tela_professor)
    notebook.pack(fill="both", expand=True, padx=20, pady=10)

    # ===================== ABA 1: GERENCIAR NOTAS =====================
    frame_notas = tk.Frame(notebook, bg="#ecf0f1")
    notebook.add(frame_notas, text="📊 Gerenciar Notas")

    # Frame de controle
    controle_frame = tk.Frame(frame_notas, bg="#ecf0f1")
    controle_frame.pack(fill="x", padx=20, pady=10)

    # Combobox para selecionar disciplina
    tk.Label(controle_frame, text="Selecionar Disciplina:", bg="#ecf0f1", 
             font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))

    disciplinas_var = tk.StringVar()
    disciplinas_combo = ttk.Combobox(controle_frame, textvariable=disciplinas_var,
                                    values=[disc["nome"] for disc in disciplinas_professor],
                                    width=30, state="readonly")
    disciplinas_combo.pack(side="left", padx=(0, 20))
    
    if disciplinas_professor:
        disciplinas_combo.set(disciplinas_professor[0]["nome"])

    # Botão para adicionar nota
    btn_adicionar_nota = tk.Button(controle_frame, text="➕ Adicionar Nota", bg="#4CAF50", fg="white",
                                 font=("Arial", 10, "bold"), command=lambda: abrir_tela_notas_professor(tela_professor, nome_professor))
    btn_adicionar_nota.pack(side="left", padx=5)

    # Botão para atualizar lista
    def atualizar_lista_notas():
        disciplina_selecionada = disciplinas_var.get()
        if not disciplina_selecionada:
            return
        
        # Limpar tabela
        for item in tree_notas.get_children():
            tree_notas.delete(item)
        
        # Buscar notas da disciplina selecionada
        notas_disciplina = [nota for nota in notas if nota.get('disciplina') == disciplina_selecionada]
        
        # Buscar alunos da turma da disciplina
        turma_disciplina = None
        for disc in disciplinas_professor:
            if disc["nome"] == disciplina_selecionada:
                turma_disciplina = disc["turma"]
                break
        
        if not turma_disciplina:
            return
        
        alunos_turma = [aluno for aluno in alunos if aluno["turma"] == turma_disciplina]
        
        # Inserir dados na tabela
        for aluno in alunos_turma:
            # Procurar nota do aluno nesta disciplina
            nota_aluno = None
            for nota in notas_disciplina:
                if nota.get("aluno") == aluno["nome"]:
                    nota_aluno = nota
                    break
            
            np1 = nota_aluno.get("np1", "-") if nota_aluno else "-"
            np2 = nota_aluno.get("np2", "-") if nota_aluno else "-"
            
            # Calcular média
            if np1 != "-" and np2 != "-":
                try:
                    media = (float(np1) + float(np2)) / 2
                    media_str = f"{media:.1f}"
                    status = "Aprovado" if media >= 6.0 else "Recuperação" if media >= 4.0 else "Reprovado"
                except:
                    media_str = "-"
                    status = "Cursando"
            else:
                media_str = "-"
                status = "Cursando"
            
            tree_notas.insert("", "end", values=(
                aluno["nome"],
                aluno["RA"],
                aluno["turma"],
                np1,
                np2,
                media_str,
                status
            ), tags=(status,))

    btn_atualizar = tk.Button(controle_frame, text="🔄 Atualizar Lista", bg="#3498db", fg="white",
                            font=("Arial", 10, "bold"), command=atualizar_lista_notas)
    btn_atualizar.pack(side="left", padx=5)

    # Frame da tabela de notas
    frame_tabela_notas = tk.Frame(frame_notas, bg="#ecf0f1")
    frame_tabela_notas.pack(fill="both", expand=True, padx=20, pady=10)

    # Tabela de notas
    tree_notas = ttk.Treeview(frame_tabela_notas, 
                             columns=("Aluno", "RA", "Turma", "NP1", "NP2", "Média", "Status"),
                             show="headings", height=15)

    tree_notas.heading("Aluno", text="Aluno")
    tree_notas.heading("RA", text="RA")
    tree_notas.heading("Turma", text="Turma")
    tree_notas.heading("NP1", text="NP1")
    tree_notas.heading("NP2", text="NP2")
    tree_notas.heading("Média", text="Média")
    tree_notas.heading("Status", text="Status")

    tree_notas.column("Aluno", width=200, anchor="center")
    tree_notas.column("RA", width=120, anchor="center")
    tree_notas.column("Turma", width=80, anchor="center")
    tree_notas.column("NP1", width=80, anchor="center")
    tree_notas.column("NP2", width=80, anchor="center")
    tree_notas.column("Média", width=80, anchor="center")
    tree_notas.column("Status", width=100, anchor="center")

    # Configurar cores para os status
    tree_notas.tag_configure("Aprovado", background="#d5f4e6")
    tree_notas.tag_configure("Recuperação", background="#fcf3cd")
    tree_notas.tag_configure("Reprovado", background="#fadbd8")
    tree_notas.tag_configure("Cursando", background="#d6eaf8")

    v_scrollbar1 = ttk.Scrollbar(frame_tabela_notas, orient="vertical", command=tree_notas.yview)
    h_scrollbar1 = ttk.Scrollbar(frame_tabela_notas, orient="horizontal", command=tree_notas.xview)
    tree_notas.configure(yscrollcommand=v_scrollbar1.set, xscrollcommand=h_scrollbar1.set)

    tree_notas.grid(row=0, column=0, sticky="nsew")
    v_scrollbar1.grid(row=0, column=1, sticky="ns")
    h_scrollbar1.grid(row=1, column=0, sticky="ew")

    frame_tabela_notas.grid_rowconfigure(0, weight=1)
    frame_tabela_notas.grid_columnconfigure(0, weight=1)

    # Função para editar nota com duplo clique
    def editar_nota_professor(event):
        item = tree_notas.selection()[0] if tree_notas.selection() else None
        if not item:
            return
        
        valores = tree_notas.item(item, 'values')
        aluno_nome, ra, turma, np1, np2, media, status = valores
        
        # Criar janela de edição
        editar_janela = tk.Toplevel(tela_professor)
        editar_janela.title(f"Editar Notas - {aluno_nome}")
        editar_janela.geometry("400x300")
        editar_janela.configure(bg="#dcdcdc")
        editar_janela.resizable(False, False)
        editar_janela.transient(tela_professor)
        editar_janela.grab_set()
        
        # Centralizar janela
        editar_janela.update_idletasks()
        x = (editar_janela.winfo_screenwidth() // 2) - (editar_janela.winfo_width() // 2)
        y = (editar_janela.winfo_screenheight() // 2) - (editar_janela.winfo_height() // 2)
        editar_janela.geometry(f"+{x}+{y}")
        
        main_frame = tk.Frame(editar_janela, bg="#dcdcdc")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(main_frame, text=f"Editar notas de {aluno_nome}", 
                bg="#dcdcdc", font=("Arial", 14, "bold")).pack(pady=(0, 10))
        
        tk.Label(main_frame, text=f"Disciplina: {disciplinas_var.get()} | Turma: {turma}", 
                bg="#dcdcdc", font=("Arial", 11)).pack(pady=5)
        
        # Frame para NP1
        np1_frame = tk.Frame(main_frame, bg="#dcdcdc")
        np1_frame.pack(fill="x", pady=10)
        
        tk.Label(np1_frame, text="NP1:", bg="#dcdcdc", 
                font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))
        
        notas_opcoes = ["-", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0"]
        np1_var = tk.StringVar(value=np1)
        np1_combobox = ttk.Combobox(np1_frame, textvariable=np1_var,
                                   values=notas_opcoes, width=10, state="readonly")
        np1_combobox.pack(side="left")
        
        # Frame para NP2
        np2_frame = tk.Frame(main_frame, bg="#dcdcdc")
        np2_frame.pack(fill="x", pady=10)
        
        tk.Label(np2_frame, text="NP2:", bg="#dcdcdc", 
                font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))
        
        np2_var = tk.StringVar(value=np2)
        np2_combobox = ttk.Combobox(np2_frame, textvariable=np2_var,
                                   values=notas_opcoes, width=10, state="readonly")
        np2_combobox.pack(side="left")
        
        # Label para mostrar a média calculada
        media_label = tk.Label(main_frame, text="Média: --", 
                              bg="#dcdcdc", font=("Arial", 11, "bold"))
        media_label.pack(pady=10)
        
        # Função para calcular média em tempo real
        def calcular_media():
            np1_val = np1_var.get()
            np2_val = np2_var.get()
            
            if np1_val != "-" and np2_val != "-":
                try:
                    media_val = (float(np1_val) + float(np2_val)) / 2
                    media_label.config(text=f"Média: {media_val:.1f}")
                    
                    # Colorir conforme a média
                    if media_val >= 6.0:
                        media_label.config(fg="#27ae60")  # Verde
                    elif media_val >= 4.0:
                        media_label.config(fg="#f39c12")  # Laranja
                    else:
                        media_label.config(fg="#e74c3c")  # Vermelho
                except ValueError:
                    media_label.config(text="Média: --", fg="#2c3e50")
            else:
                media_label.config(text="Média: --", fg="#2c3e50")
        
        # Vincular o cálculo da média às comboboxes
        np1_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())
        np2_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())
        
        # Frame dos botões
        btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
        btn_frame.pack(pady=20)
        
        def salvar_edicao():
            np1_val = np1_var.get()
            np2_val = np2_var.get()
            
            # Atualizar nos dados
            notas_atualizadas = carregar_notas()
            nota_encontrada = False
            
            for nota in notas_atualizadas:
                if (nota.get('aluno') == aluno_nome and 
                    nota.get('disciplina') == disciplinas_var.get()):
                    
                    nota['np1'] = np1_val
                    nota['np2'] = np2_val
                    nota_encontrada = True
                    break
            
            # Se não encontrou, criar nova nota
            if not nota_encontrada:
                notas_atualizadas.append({
                    "aluno": aluno_nome,
                    "turma": turma,
                    "disciplina": disciplinas_var.get(),
                    "np1": np1_val,
                    "np2": np2_val
                })
            
            salvar_notas(notas_atualizadas)
            
            # Atualizar na tabela
            if np1_val != "-" and np2_val != "-":
                nova_media = (float(np1_val) + float(np2_val)) / 2
                novo_status = "Aprovado" if nova_media >= 6.0 else "Recuperação" if nova_media >= 4.0 else "Reprovado"
            else:
                nova_media = "-"
                novo_status = "Cursando"
            
            tree_notas.item(item, values=(
                aluno_nome, ra, turma, np1_val, np2_val, 
                f"{nova_media:.1f}" if nova_media != "-" else "-", 
                novo_status
            ), tags=(novo_status,))
            
            messagebox.showinfo("Sucesso", "Notas atualizadas com sucesso!")
            editar_janela.destroy()
        
        def cancelar_edicao():
            editar_janela.destroy()
        
        btn_salvar = tk.Button(btn_frame, text="Salvar", bg="#4CAF50", fg="white",
                             font=("Arial", 10, "bold"), width=12,
                             command=salvar_edicao)
        btn_salvar.pack(side="left", padx=5)
        
        btn_cancelar = tk.Button(btn_frame, text="Cancelar", bg="#e74c3c", fg="white",
                               font=("Arial", 10, "bold"), width=12,
                               command=cancelar_edicao)
        btn_cancelar.pack(side="left", padx=5)
        
        # Calcular média inicial
        calcular_media()

    tree_notas.bind("<Double-1>", editar_nota_professor)

    # Atualizar lista quando selecionar disciplina
    disciplinas_combo.bind('<<ComboboxSelected>>', lambda e: atualizar_lista_notas())

    # ===================== ABA 2: VISUALIZAR ALUNOS =====================
    frame_alunos = tk.Frame(notebook, bg="#ecf0f1")
    notebook.add(frame_alunos, text="👥 Visualizar Alunos")

    # Frame de filtro
    filtro_frame = tk.Frame(frame_alunos, bg="#ecf0f1")
    filtro_frame.pack(fill="x", padx=20, pady=10)

    tk.Label(filtro_frame, text="Filtrar por Turma:", bg="#ecf0f1", 
             font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))

    # Obter turmas das disciplinas do professor
    turmas_professor = list(set([disc["turma"] for disc in disciplinas_professor]))
    turmas_var = tk.StringVar(value="Todas as Turmas")
    turmas_combo = ttk.Combobox(filtro_frame, textvariable=turmas_var,
                               values=["Todas as Turmas"] + turmas_professor,
                               width=20, state="readonly")
    turmas_combo.pack(side="left", padx=(0, 20))

    # Frame da tabela de alunos
    frame_tabela_alunos = tk.Frame(frame_alunos, bg="#ecf0f1")
    frame_tabela_alunos.pack(fill="both", expand=True, padx=20, pady=10)

    # Tabela de alunos (somente visualização)
    tree_alunos = ttk.Treeview(frame_tabela_alunos, 
                              columns=("Nome", "RA", "Turma", "Curso", "Email"),
                              show="headings", height=15)

    tree_alunos.heading("Nome", text="Nome")
    tree_alunos.heading("RA", text="RA")
    tree_alunos.heading("Turma", text="Turma")
    tree_alunos.heading("Curso", text="Curso")
    tree_alunos.heading("Email", text="Email")

    tree_alunos.column("Nome", width=250, anchor="center")
    tree_alunos.column("RA", width=120, anchor="center")
    tree_alunos.column("Turma", width=80, anchor="center")
    tree_alunos.column("Curso", width=200, anchor="center")
    tree_alunos.column("Email", width=150, anchor="center")

    v_scrollbar2 = ttk.Scrollbar(frame_tabela_alunos, orient="vertical", command=tree_alunos.yview)
    h_scrollbar2 = ttk.Scrollbar(frame_tabela_alunos, orient="horizontal", command=tree_alunos.xview)
    tree_alunos.configure(yscrollcommand=v_scrollbar2.set, xscrollcommand=h_scrollbar2.set)

    tree_alunos.grid(row=0, column=0, sticky="nsew")
    v_scrollbar2.grid(row=0, column=1, sticky="ns")
    h_scrollbar2.grid(row=1, column=0, sticky="ew")

    frame_tabela_alunos.grid_rowconfigure(0, weight=1)
    frame_tabela_alunos.grid_columnconfigure(0, weight=1)

    # Função para carregar alunos
    def carregar_alunos_visualizacao():
        turma_selecionada = turmas_var.get()
        
        # Limpar tabela
        for item in tree_alunos.get_children():
            tree_alunos.delete(item)
        
        # Filtrar alunos
        if turma_selecionada == "Todas as Turmas":
            alunos_filtrados = [aluno for aluno in alunos if any(
                disc["turma"] == aluno["turma"] for disc in disciplinas_professor
            )]
        else:
            alunos_filtrados = [aluno for aluno in alunos if aluno["turma"] == turma_selecionada]
        
        # Inserir alunos na tabela
        for aluno in alunos_filtrados:
            tree_alunos.insert("", "end", values=(
                aluno["nome"],
                aluno["RA"],
                aluno["turma"],
                aluno["curso"],
                aluno.get("email", aluno["RA"])
            ))

    # Carregar alunos inicialmente
    carregar_alunos_visualizacao()

    # Atualizar quando mudar a turma
    turmas_combo.bind('<<ComboboxSelected>>', lambda e: carregar_alunos_visualizacao())

    # ===================== ABA 3: CONTEÚDOS =====================
    frame_conteudos = tk.Frame(notebook, bg="#ecf0f1")
    notebook.add(frame_conteudos, text="📚 Meus Conteúdos")

    # Frame de controle de conteúdos
    controle_conteudos_frame = tk.Frame(frame_conteudos, bg="#ecf0f1")
    controle_conteudos_frame.pack(fill="x", padx=20, pady=10)

    btn_adicionar_conteudo = tk.Button(controle_conteudos_frame, text="➕ Adicionar Conteúdo", 
                                     bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                                     command=lambda: abrir_tela_conteudos_professor(tela_professor, nome_professor))
    btn_adicionar_conteudo.pack(side="left", padx=5)

    # Frame da tabela de conteúdos
    frame_tabela_conteudos = tk.Frame(frame_conteudos, bg="#ecf0f1")
    frame_tabela_conteudos.pack(fill="both", expand=True, padx=20, pady=10)

    # Tabela de conteúdos do professor
    tree_conteudos = ttk.Treeview(frame_tabela_conteudos, 
                                 columns=("Disciplina", "Título", "Tipo", "Data", "Arquivo"),
                                 show="headings", height=15)

    tree_conteudos.heading("Disciplina", text="Disciplina")
    tree_conteudos.heading("Título", text="Título")
    tree_conteudos.heading("Tipo", text="Tipo")
    tree_conteudos.heading("Data", text="Data")
    tree_conteudos.heading("Arquivo", text="Arquivo")

    tree_conteudos.column("Disciplina", width=150, anchor="center")
    tree_conteudos.column("Título", width=200, anchor="center")
    tree_conteudos.column("Tipo", width=120, anchor="center")
    tree_conteudos.column("Data", width=100, anchor="center")
    tree_conteudos.column("Arquivo", width=150, anchor="center")

    v_scrollbar3 = ttk.Scrollbar(frame_tabela_conteudos, orient="vertical", command=tree_conteudos.yview)
    h_scrollbar3 = ttk.Scrollbar(frame_tabela_conteudos, orient="horizontal", command=tree_conteudos.xview)
    tree_conteudos.configure(yscrollcommand=v_scrollbar3.set, xscrollcommand=h_scrollbar3.set)

    tree_conteudos.grid(row=0, column=0, sticky="nsew")
    v_scrollbar3.grid(row=0, column=1, sticky="ns")
    h_scrollbar3.grid(row=1, column=0, sticky="ew")

    frame_tabela_conteudos.grid_rowconfigure(0, weight=1)
    frame_tabela_conteudos.grid_columnconfigure(0, weight=1)

    # Carregar conteúdos do professor
    def carregar_conteudos_professor():
        # Limpar tabela
        for item in tree_conteudos.get_children():
            tree_conteudos.delete(item)
        
        # Filtrar conteúdos pelas disciplinas do professor
        disciplinas_nomes = [disc["nome"] for disc in disciplinas_professor]
        conteudos_professor = [cont for cont in conteudos if cont.get("disciplina") in disciplinas_nomes]
        
        for cont in conteudos_professor:
            arquivo = "📎 Disponível" if cont.get('arquivo') and cont.get('arquivo') != '-' else "Não há"
            tree_conteudos.insert("", "end", values=(
                cont.get('disciplina', '-'),
                cont.get('titulo', '-'),
                cont.get('tipo', '-'),
                cont.get('data', '-'),
                arquivo
            ))

    carregar_conteudos_professor()

    # ===================== ABA 4: INFORMAÇÕES =====================
    frame_info = tk.Frame(notebook, bg="#ecf0f1")
    notebook.add(frame_info, text="👤 Informações do Professor")

    # Frame das informações
    info_professor_frame = tk.Frame(frame_info, bg="#ecf0f1")
    info_professor_frame.pack(fill="both", expand=True, padx=50, pady=30)

    # Card de informações
    card_frame = tk.Frame(info_professor_frame, bg="white", relief="solid", bd=1)
    card_frame.pack(fill="both", expand=True)

    # Título do card
    tk.Label(card_frame, text="Dados do Professor", bg="#34495e", fg="white",
             font=("Arial", 14, "bold"), pady=10).pack(fill="x")

    # Conteúdo do card
    content_frame = tk.Frame(card_frame, bg="white", padx=20, pady=20)
    content_frame.pack(fill="both", expand=True)

    info_labels = [
        ("Nome:", f"Prof. {nome_professor}"),
        ("Disciplinas:", f"{len(disciplinas_professor)} disciplina(s)"),
        ("Turmas:", ", ".join(set([disc["turma"] for disc in disciplinas_professor]))),
        ("Total de Alunos:", f"{sum(len([a for a in alunos if a['turma'] == disc['turma']]) for disc in disciplinas_professor)} alunos")
    ]

    for i, (label, value) in enumerate(info_labels):
        row_frame = tk.Frame(content_frame, bg="white")
        row_frame.pack(fill="x", pady=8)
        
        tk.Label(row_frame, text=label, bg="white", font=("Arial", 11, "bold"), 
                width=15, anchor="w").pack(side="left")
        tk.Label(row_frame, text=value, bg="white", font=("Arial", 11),
                width=30, anchor="w").pack(side="left")

    # Resumo das disciplinas
    tk.Label(content_frame, text="Disciplinas Ministradas", bg="white", 
             font=("Arial", 12, "bold"), pady=(20, 10)).pack(fill="x")

    for disc in disciplinas_professor:
        disc_frame = tk.Frame(content_frame, bg="white")
        disc_frame.pack(fill="x", pady=5)
        
        alunos_turma = len([a for a in alunos if a["turma"] == disc["turma"]])
        
        tk.Label(disc_frame, text=f"• {disc['nome']} ({disc['turma']}) - {alunos_turma} alunos", 
                bg="white", font=("Arial", 10)).pack(anchor="w")

    # ===================== RODAPÉ =====================
    footer = tk.Frame(tela_professor, bg="#2c3e50", height=30)
    footer.pack(fill="x", side="bottom")
    
    tk.Label(footer, text=f"© 2025 Sistema Acadêmico - Professor {nome_professor}", 
             bg="#2c3e50", fg="#bdc3c7", font=("Arial", 9)).pack(pady=5)

    # Atualizar lista de notas inicialmente
    if disciplinas_professor:
        atualizar_lista_notas()

    tela_professor.focus_force()
    tela_professor.lift()
    tela_professor.mainloop()
# ===================== FUNÇÃO PARA CADASTRAR NOTAS (PROFESSOR) =====================
def abrir_tela_notas_professor(parent_window, nome_professor):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Notas - Professor")
    janela_cadastro.geometry("500x500")
    janela_cadastro.config(bg="#dcdcdc")
    janela_cadastro.resizable(False, False)

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Notas", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Carregar dados
    disciplinas = carregar_disciplinas()
    alunos = carregar_alunos()
    
    # Filtrar disciplinas do professor
    disciplinas_professor = [disc for disc in disciplinas if disc.get("professor") == nome_professor]

    # Formulário em grid
    tk.Label(main_frame, text="Disciplina:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
    disciplinas_nomes = [disc["nome"] for disc in disciplinas_professor]
    disciplina_combobox = ttk.Combobox(main_frame, values=disciplinas_nomes, width=28, font=("Arial", 10))
    disciplina_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=8)
    if disciplinas_nomes:
        disciplina_combobox.set(disciplinas_nomes[0])

    tk.Label(main_frame, text="Aluno:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
    
    # Função para atualizar alunos baseado na disciplina selecionada
    def atualizar_alunos(event=None):
        disciplina_selecionada = disciplina_combobox.get()
        if not disciplina_selecionada:
            return
        
        # Encontrar a turma da disciplina selecionada
        turma_disciplina = None
        for disc in disciplinas_professor:
            if disc["nome"] == disciplina_selecionada:
                turma_disciplina = disc["turma"]
                break
        
        if turma_disciplina:
            # Filtrar alunos da turma
            alunos_turma = [aluno["nome"] for aluno in alunos if aluno["turma"] == turma_disciplina]
            aluno_combobox['values'] = alunos_turma
            if alunos_turma:
                aluno_combobox.set(alunos_turma[0])
            else:
                aluno_combobox.set("")

    aluno_combobox = ttk.Combobox(main_frame, width=28, font=("Arial", 10))
    aluno_combobox.grid(row=2, column=1, sticky="ew", padx=10, pady=8)
    
    # Atualizar alunos quando disciplina mudar
    disciplina_combobox.bind('<<ComboboxSelected>>', atualizar_alunos)
    
    # Atualizar alunos inicialmente
    atualizar_alunos()

    tk.Label(main_frame, text="NP1:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
    
    notas_opcoes = ["-", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0"]
    np1_combobox = ttk.Combobox(main_frame, values=notas_opcoes, width=28, font=("Arial", 10))
    np1_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=8)
    np1_combobox.set("-")

    tk.Label(main_frame, text="NP2:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=8)
    
    np2_combobox = ttk.Combobox(main_frame, values=notas_opcoes, width=28, font=("Arial", 10))
    np2_combobox.grid(row=4, column=1, sticky="ew", padx=10, pady=8)
    np2_combobox.set("-")

    # Label para mostrar a média calculada
    media_label = tk.Label(main_frame, text="Média: --", bg="#dcdcdc", 
                          font=("Arial", 11, "bold"), fg="#2c3e50")
    media_label.grid(row=5, column=0, columnspan=2, pady=10)

    # Função para calcular e mostrar a média
    def calcular_media():
        np1 = np1_combobox.get().strip()
        np2 = np2_combobox.get().strip()
        
        if np1 != "-" and np2 != "-":
            try:
                media = (float(np1) + float(np2)) / 2
                media_label.config(text=f"Média: {media:.1f}")
                
                # Colorir conforme a média
                if media >= 6.0:
                    media_label.config(fg="#27ae60")  # Verde
                elif media >= 4.0:
                    media_label.config(fg="#f39c12")  # Laranja
                else:
                    media_label.config(fg="#e74c3c")  # Vermelho
            except ValueError:
                media_label.config(text="Média: --", fg="#2c3e50")
        else:
            media_label.config(text="Média: --", fg="#2c3e50")

    # Vincular o cálculo da média às comboboxes
    np1_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())
    np2_combobox.bind('<<ComboboxSelected>>', lambda e: calcular_media())

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=6, column=0, columnspan=2, pady=25)

    def adicionar_nota():
        disciplina = disciplina_combobox.get().strip()
        aluno = aluno_combobox.get().strip()
        np1 = np1_combobox.get().strip()
        np2 = np2_combobox.get().strip()

        if not disciplina or not aluno:
            messagebox.showwarning("Campos obrigatórios", "Selecione a disciplina e o aluno!")
            return

        # Encontrar turma do aluno
        turma_aluno = None
        for a in alunos:
            if a["nome"] == aluno:
                turma_aluno = a["turma"]
                break

        if not turma_aluno:
            messagebox.showerror("Erro", "Turma do aluno não encontrada!")
            return

        notas = carregar_notas()
        
        # Verificar se já existe nota para este aluno nesta disciplina
        nota_existente = any(
            n.get('aluno') == aluno and 
            n.get('disciplina') == disciplina 
            for n in notas
        )
        
        if nota_existente:
            messagebox.showwarning("Registro duplicado", "Já existe uma nota cadastrada para este aluno nesta disciplina!")
            return

        notas.append({
            "aluno": aluno,
            "turma": turma_aluno,
            "disciplina": disciplina,
            "np1": np1,
            "np2": np2
        })
        salvar_notas(notas)

        messagebox.showinfo("Sucesso", "Notas cadastradas com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    def voltar_menu():
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    def criar_botao_hover(parent, texto, cor_normal, comando=None, width=15):
        btn = tk.Button(parent, text=texto, bg=cor_normal, fg="white",
                       font=("Arial", 10, "bold"), relief="raised", width=width,
                       command=comando)
        
        def on_enter(e):
            btn.config(bg="#90EE90", font=("Arial", 10, "bold"))
        
        def on_leave(e):
            btn.config(bg=cor_normal, font=("Arial", 10, "bold"))
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    btn_add_nota = criar_botao_hover(btn_frame, "Adicionar Notas", "#4CAF50", adicionar_nota)
    btn_add_nota.pack(side="left", padx=10)

    btn_voltar = criar_botao_hover(btn_frame, "Voltar", "#3498db", voltar_menu)
    btn_voltar.pack(side="left", padx=10)

    # Focar no primeiro campo
    disciplina_combobox.focus_set()

    return janela_cadastro

# ===================== FUNÇÃO PARA CADASTRAR CONTEÚDOS (PROFESSOR) =====================
def abrir_tela_conteudos_professor(parent_window, nome_professor):
    if parent_window:
        parent_window.withdraw()
        
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Conteúdo - Professor")
    janela_cadastro.geometry("600x600")
    janela_cadastro.config(bg="#dcdcdc")
    janela_cadastro.resizable(False, False)

    main_frame = tk.Frame(janela_cadastro, bg="#dcdcdc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(main_frame, text="Cadastro de Conteúdo", bg="#dcdcdc",
             font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Carregar disciplinas do professor
    disciplinas = carregar_disciplinas()
    disciplinas_professor = [disc for disc in disciplinas if disc.get("professor") == nome_professor]

    # Formulário em grid
    tk.Label(main_frame, text="Disciplina:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
    disciplinas_nomes = [disc["nome"] for disc in disciplinas_professor]
    disciplina_combobox = ttk.Combobox(main_frame, values=disciplinas_nomes, width=40, font=("Arial", 10))
    disciplina_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=8)
    if disciplinas_nomes:
        disciplina_combobox.set(disciplinas_nomes[0])

    tk.Label(main_frame, text="Título do Conteúdo:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
    titulo_entry = ttk.Entry(main_frame, width=40, font=("Arial", 10))
    titulo_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=8)

    tk.Label(main_frame, text="Tipo de Conteúdo:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
    tipo_opcoes = ["Aula Teórica", "Aula Prática", "Material de Estudo", "Exercícios", "Projeto", "Calendário", "Plano de Ensino"]
    tipo_combobox = ttk.Combobox(main_frame, values=tipo_opcoes, width=40, font=("Arial", 10))
    tipo_combobox.grid(row=3, column=1, sticky="ew", padx=10, pady=8)
    tipo_combobox.set("")

    # Data (simplificada)
    tk.Label(main_frame, text="Data:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=8)
    data_entry = ttk.Entry(main_frame, width=40, font=("Arial", 10))
    data_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=8)
    data_entry.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))

    # Descrição
    tk.Label(main_frame, text="Descrição:", bg="#dcdcdc", font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="w", pady=8)
    descricao_text = tk.Text(main_frame, wrap="word", width=40, height=6,
                           font=("Arial", 10), bg="white", relief="solid", bd=1)
    descricao_text.grid(row=5, column=1, sticky="ew", padx=10, pady=8)

    main_frame.grid_columnconfigure(1, weight=1)

    btn_frame = tk.Frame(main_frame, bg="#dcdcdc")
    btn_frame.grid(row=6, column=0, columnspan=2, pady=25)

    def adicionar_conteudo():
        disciplina = disciplina_combobox.get().strip()
        titulo = titulo_entry.get().strip()
        tipo = tipo_combobox.get().strip()
        data = data_entry.get().strip()
        descricao = descricao_text.get("1.0", "end-1c").strip()

        if not disciplina or not titulo or not tipo or not data:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos obrigatórios!")
            return

        conteudos = carregar_conteudos()
        
        # Verificar se já existe conteúdo com mesmo título e disciplina
        conteudo_existente = any(
            cont.get('disciplina') == disciplina and 
            cont.get('titulo') == titulo 
            for cont in conteudos
        )
        
        if conteudo_existente:
            messagebox.showwarning("Conteúdo duplicado", "Já existe um conteúdo com este título para esta disciplina!")
            return

        novo_conteudo = {
            "disciplina": disciplina,
            "titulo": titulo,
            "tipo": tipo,
            "data": data,
            "descricao": descricao,
            "arquivo": "-",
            "data_cadastro": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        conteudos.append(novo_conteudo)
        salvar_conteudos(conteudos)

        messagebox.showinfo("Sucesso", "Conteúdo cadastrado com sucesso!")
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    def voltar_menu():
        janela_cadastro.destroy()
        if parent_window:
            parent_window.deiconify()

    def criar_botao_hover(parent, texto, cor_normal, comando=None, width=15):
        btn = tk.Button(parent, text=texto, bg=cor_normal, fg="white",
                       font=("Arial", 10, "bold"), relief="raised", width=width,
                       command=comando)
        
        def on_enter(e):
            btn.config(bg="#90EE90", font=("Arial", 10, "bold"))
        
        def on_leave(e):
            btn.config(bg=cor_normal, font=("Arial", 10, "bold"))
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    btn_add_conteudo = criar_botao_hover(btn_frame, "Adicionar Conteúdo", "#4CAF50", adicionar_conteudo)
    btn_add_conteudo.pack(side="left", padx=10)

    btn_voltar = criar_botao_hover(btn_frame, "Voltar", "#3498db", voltar_menu)
    btn_voltar.pack(side="left", padx=10)

    disciplina_combobox.focus_set()

    return janela_cadastro

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
        
        # CORREÇÃO: Apagar apenas o container, não a logo
        canvas.delete("container")
        
        # Desenhar container PRIMEIRO (fundo)
        round_rect(canvas, frame_x, frame_y, frame_x+container_width, frame_y+container_height,
                   radius=20, fill="#6a5acd", outline="#6a5acd", tags="container")
        return frame_x, frame_y

    frame_x, frame_y = container_wi()

    # CORREÇÃO: Carregar a logo DEPOIS do container e com tag específica
    logo_path = os.path.join(os.getcwd(), "IMG", "Logo.png")
    
    try:
        img = Image.open(logo_path).resize((135, 125), Image.Resampling.LANCZOS)
        root.logo_img = ImageTk.PhotoImage(img)
        
        # CORREÇÃO: Posicionar a logo ACIMA do container
        logo = canvas.create_image(frame_x + container_width//2, frame_y + 60, 
                                   image=root.logo_img, tags=("logo", "above_container"))
        print(f"✅ Logo carregada com sucesso: {logo_path}")
        
        # CORREÇÃO: Garantir que a logo fique acima do container
        canvas.tag_raise("logo")
        
    except Exception as e:
        print(f"❌ Erro ao carregar logo: {e}")
        # Fallback - criar um logo com texto
        logo = canvas.create_text(frame_x + container_width//2, frame_y + 60, 
                                text="🎓", font=("Arial", 40), fill="white", tags=("logo", "above_container"))
        canvas.tag_raise("logo")

    def create_entry(parent, placeholder="", is_password=False):
        entry = tk.Entry(parent, bd=0, bg="#ffffff", fg="gray", font=("Arial", 12), highlightthickness=1, highlightcolor="#6a5acd")
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

    # Criar campos de entrada
    email_entry = create_entry(root, placeholder="Código da Matéria ou RA")
    senha_entry = create_entry(root, placeholder="Senha", is_password=True)

    def login():
        usuario = email_entry.get().strip()
        senha = senha_entry.get().strip()
        users = load_users()
        
        if usuario in users and users[usuario] == senha:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
            root.destroy()
        
            if usuario == "admin":
                abrir_tela_admin()
            elif usuario in ["ENG001", "PYT002", "CPP003", "BD004", "RED005", "SO006", "ED007", "IA008"]:
                disciplinas = carregar_disciplinas()
                professor = None
                for disc in disciplinas:
                    if disc.get('codigo') == usuario:
                        professor = disc.get('professor')
                        break
                
                if professor:
                    abrir_tela_professor(professor)
                else:
                    messagebox.showerror("Erro", "Professor não encontrado para esta matéria!")
            else:
                abrir_tela_aluno(usuario)
        else:
            messagebox.showerror("Erro", "Código da matéria/RA ou senha incorretos!")

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
                         font=("Arial", 12, "bold"), bd=0, relief="flat", 
                         cursor="hand2", command=command)
        
        def on_enter(e):
            btn.config(bg="#f0f0f0" if bg_color == "#ffffff" else "#34495e")
        
        def on_leave(e):
            btn.config(bg=bg_color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn

    # Criar botões
    login_btn = create_button(root, "Login", command=login)
    register_btn = create_button(root, "Cadastrar", bg_color="#27ae60", fg_color="white", command=register)
    fb_btn = create_button(root, "f", bg_color="#3b5998", fg_color="white", command=facebook_login)
    google_btn = create_button(root, "G", bg_color="#db4437", fg_color="white", command=google_login)

    # Adicionar textos informativos no canvas
    canvas.create_text(frame_x + container_width//2, frame_y + 320, 
                      text="Ou entre com", fill="white", font=("Arial", 10), tags="social_text")

    def update_layout(event=None):
        frame_x, frame_y = container_wi()
        
        # CORREÇÃO: Atualizar posição da logo primeiro
        canvas.coords(logo, frame_x + container_width//2, frame_y + 60)
        
        # CORREÇÃO: Garantir que logo fique sempre acima
        canvas.tag_raise("logo")
        
        # Atualizar textos
        canvas.coords("social_text", frame_x + container_width//2, frame_y + 320)
        
        # Posicionar widgets
        email_entry.place(x=frame_x + 40, y=frame_y + 140, width=270, height=35)
        senha_entry.place(x=frame_x + 40, y=frame_y + 200, width=270, height=35)
        login_btn.place(x=frame_x + 40, y=frame_y + 260, width=130, height=40)
        register_btn.place(x=frame_x + 180, y=frame_y + 260, width=130, height=40)
        fb_btn.place(x=frame_x + int(container_width*0.25)-25, y=frame_y + 350, width=50, height=35)
        google_btn.place(x=frame_x + int(container_width*0.75)-25, y=frame_y + 350, width=50, height=35)

    root.bind("<Configure>", update_layout)
    update_layout()

    # Footer
    footer = tk.Label(root, text="© 2025 Minha Aplicação", bg="#2c3e50", fg="#bdc3c7", font=("Arial", 10))
    footer.pack(side="bottom", pady=10)

    # Atalhos de teclado
    email_entry.bind("<Return>", lambda e: login())
    senha_entry.bind("<Return>", lambda e: login())

    # Focar no campo de email inicialmente
    email_entry.focus_set()

    root.mainloop()

if __name__ == "__main__":
    inicializar_sistema()  
    main_login_window()