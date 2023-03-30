import rpa as r
import pyautogui as p
import requests
import pandas as pd

            # INICIALIZANDO NAVEGAÇÃO
r.init(turbo_mode=True)
r.url('http://rpachallenge.com')
r.wait(7.0)

            # MAXIMIZANDO
janela = p.getActiveWindow()
janela.maximize()

            # FAZENDO DONWLOAD DO ARQUIVO
url = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx' # Endereço do arquivo
requisicao = requests.get(url, allow_redirects=True) #Solicitando requisição para a pagina

open('rpaTesteDownload.xlsx', 'wb').write(requisicao.content) #Dando nome e escrevendo dados no arquivo

            #LENDO ARQUIVO
dados = pd.read_excel('rpaTesteDownload.xlsx',sheet_name='Sheet1') # Leitura do arquivo , Nome da planilha

            #TRANSFORMANDO EM UM DATAFRAME
df_dados = pd.DataFrame(dados , columns=['First Name','Last Name ','Company Name','Role in Company','Address','Email','Phone Number'])

            #INICIANDO DESAFIO
r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')  # XPATH ESTATICO

            #INSERINDO DADOS (ELEMENTOS NÃO SÃO ESTATICOS)
for linha in df_dados.itertuples() : #.itertuples() a primeira linha da tabela vai ser pra armazenada pra linha
    r.type('//*[@ng-reflect-name="labelFirstName"]',linha[1])
    r.type('//*[@ng-reflect-name="labelLastName"]', linha[2])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', linha[3])
    r.type('//*[@ng-reflect-name="labelRole"]', linha[4])
    r.type('//*[@ng-reflect-name="labelAddress"]', linha[5])
    r.type('//*[@ng-reflect-name="labelEmail"]',linha[6])
    r.type('//*[@ng-reflect-name="labelPhone"]', str(linha[7]))

    r.click('//*[@class="btn uiColorButton"]')

r.wait(2.0)
p.screenshot('Resultado.PNG')
janela.close()