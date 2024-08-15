import pandas as pd
import pyautogui
import time
import webbrowser
import pyperclip
import csv

pyautogui.PAUSE = 3

tabela = pd.read_csv(r"C:\Users\Winlitepro\Desktop\lista de cnpj.csv", dtype={'cnpj': str})

home = 'https://casadosdados.com.br/solucao/cnpj?q='

dados = []

for linha in tabela.index:
    empresa = tabela.loc[linha, 'cnpj']
    emp = str(empresa)[1:]
    url = home + emp
    webbrowser.open(url)
    time.sleep(3)
    pyautogui.press('tab', presses=6)
    pyautogui.press('enter')    
    pyautogui.click(952, 241)
    pyautogui.click(953, 241)

    pyautogui.tripleClick(670, 206)
    pyautogui.hotkey('ctrl', 'c')
    titulo = pyperclip.paste()

    pyautogui.press('tab', presses=4)

    pyautogui.tripleClick(321, 692)
    pyautogui.hotkey('ctrl', 'c')
    capital = pyperclip.paste()

    dados.append({'titulo': titulo, 'capital': capital})
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')

# Salvando os dados no CSV
with open(r"C:\Users\Winlitepro\Desktop\resultado_cnpj.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Título', 'Capital'])
    writer.writeheader()
    writer.writerows(dados)


  

  
    
        

    
