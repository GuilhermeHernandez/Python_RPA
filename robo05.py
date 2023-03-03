import rpa as r
import pyautogui as p
import pandas as pd

r.init()  # Permitindo automatização
r.url('https://rpachallengeocr.azurewebsites.net/')  # Navega até URL informada
r.wait(2.0)

janela = p.getActiveWindow()  # Retorna janela ativa por automação
janela.maximize()  # Maximiza janela automatizada
r.wait(5.0)

pagina = 1

while pagina <= 3:
    r.table('//*[@id="tableSandbox"]', 'temp.csv')  # Faz leitura da tabela e armazena em um arquivo temporario
    dados = pd.read_csv('temp.csv')  # Faz a leitura dados contido no arquivo CSV
    dados.to_csv(r'WebTable.csv', mode='a', index=None, header=True)  # Escreve os dados em uma nova tabela csv

    r.click('//*[@id="tableSandbox_next"]')
    pagina = pagina + 1

r.close()
