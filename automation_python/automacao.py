''' 
*Passo a passo do projeto

Passo 1 - Entrar no sistema
    https://dlp.hashtagtreinamentos.com/python/intensivao/tabela
Passo 2 - Fazer login
Passo 3 - Importar a base de dados
Passo 4 - Cadastrar um produto
Passo 5 - Repetir isso até acabar a base de dados


- Bibliotecas = Pacotes de ferramentas feitos por alguém que te ajuda a realizar uma tarefa.
    - Pyautogui - RPA = Automação de processos por robos (bot)
    
    # Clicar -> Pyautogui.click
    # Escrever -> Pyautogui.write
    # Apertar tecla -> Pyautogui.press 
    # Apertar -> Pyautogui.hotkey
    # rolar página -> Pyautogui.scroll (número -, rola pra baixo, +, pra cima)
    
    # tabela.loc[linha, "coluna"]
    
    # Entre "win" é o nome da tecla
    
    pip install pandas numpy openpyxl
'''

import pyautogui  # bot
import time
import pandas  # Lê arquivo


pyautogui.PAUSE = 0.5  # Todos os comandos terão espera de meio segundo

#* Passo 1 - Entrar no sistema

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")


#* Passo 2 - Fazer login

# Ir para campo de email
pyautogui.click(x=750, y=375)

# digitar email
pyautogui.write("lucas@hotmail.com")

# Ir para campo da senha
pyautogui.press("tab")

# Definir senha
pyautogui.write("senhaX123")

# Clicar no botão logar
pyautogui.click(x=939, y=530)


#* Passo 3 - Importar a base de dados

tabela = pandas.read_csv("automation_python/produtos.csv")
print(tabela)


#* Passo 4 - Cadastrar um produto

for linha in tabela.index:
    
    # clica na primeira linha
    pyautogui.click(x=709, y=258)
    
    # Código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):  # verifica se o obs é vazio, se for, só da tab, se nao, preenche com a observação conforme está na tebela
        pyautogui.write(obs)

    # Enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Para ir até o inicio da tela para voltar a cadastrar 
    pyautogui.scroll(5000)  
    