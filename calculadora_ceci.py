import tkinter as tk
from tkinter import messagebox
import math

# -----------------------------
# Funções
# -----------------------------

def adicionar(valor):
    visor.insert(tk.END, valor)


def limpar():
    visor.delete(0, tk.END)


def calcular():
    try:
        expressao = visor.get()
        resultado = eval(expressao)
        historico.insert(tk.END, f"{expressao} = {resultado}\n")
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except:
        messagebox.showerror("Erro", "Cálculo inválido!")
        limpar()


def porcentagem():
    try:
        valor = float(visor.get())
        resultado = valor / 100
        historico.insert(tk.END, f"{valor}% = {resultado}\n")
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except:
        messagebox.showerror("Erro", "Valor inválido!")


def raiz_quadrada():
    try:
        valor = float(visor.get())
        resultado = math.sqrt(valor)
        historico.insert(tk.END, f"√{valor} = {resultado}\n")
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except:
        messagebox.showerror("Erro", "Valor inválido!")


def potencia():
    try:
        valor = float(visor.get())
        resultado = valor ** 2
        historico.insert(tk.END, f"{valor}² = {resultado}\n")
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except:
        messagebox.showerror("Erro", "Valor inválido!")


# -----------------------------
# Janela
# -----------------------------

janela = tk.Tk()
janela.title("Calculadora Avançada")
janela.geometry("420x520")
janela.config(bg="#1e1e2e")
janela.resizable(False, False)

# -----------------------------
# Visor
# -----------------------------

visor = tk.Entry(
    janela,
    font=("Segoe UI", 22),
    justify="right",
    bg="#f8f8f2",
    fg="#000",
    relief="flat"
)
visor.pack(fill="x", padx=15, pady=15)

# -----------------------------
# Frame botões
# -----------------------------

frame = tk.Frame(janela, bg="#1e1e2e")
frame.pack()

botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "+", "="
]

linha = 0
coluna = 0

for botao in botoes:
    if botao == "=":
        b = tk.Button(
            frame, text=botao, font=("Segoe UI", 16),
            width=6, height=2,
            bg="#50fa7b", fg="#000",
            command=calcular
        )
    else:
        b = tk.Button(
            frame, text=botao, font=("Segoe UI", 16),
            width=6, height=2,
            bg="#44475a", fg="white",
            command=lambda v=botao: adicionar(v)
        )

    b.grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1

    if coluna == 4:
        coluna = 0
        linha += 1

# -----------------------------
# Botões extras
# -----------------------------

extras = tk.Frame(janela, bg="#1e1e2e")
extras.pack(pady=10)

tk.Button(extras, text="C", width=6, height=2,
          bg="#ff5555", fg="white", font=("Segoe UI", 14),
          command=limpar).grid(row=0, column=0, padx=5)

tk.Button(extras, text="%", width=6, height=2,
          bg="#6272a4", fg="white", font=("Segoe UI", 14),
          command=porcentagem).grid(row=0, column=1, padx=5)

tk.Button(extras, text="√", width=6, height=2,
          bg="#6272a4", fg="white", font=("Segoe UI", 14),
          command=raiz_quadrada).grid(row=0, column=2, padx=5)

tk.Button(extras, text="x²", width=6, height=2,
          bg="#6272a4", fg="white", font=("Segoe UI", 14),
          command=potencia).grid(row=0, column=3, padx=5)

# -----------------------------
# Histórico
# -----------------------------

tk.Label(janela, text="Histórico",
         bg="#1e1e2e", fg="white",
         font=("Segoe UI", 12)).pack()

historico = tk.Text(
    janela,
    height=6,
    font=("Segoe UI", 10),
    bg="#282a36",
    fg="#f8f8f2"
)
historico.pack(fill="x", padx=15, pady=10)

# -----------------------------
# Loop
# -----------------------------

janela.mainloop()