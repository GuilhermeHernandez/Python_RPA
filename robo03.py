import rpa as r
import pyautogui as p
import pandas as pd
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
r.wait(2.0)

janela = p.getActiveWindow()
janela.maximize()

dolar_comercial = r.read('//*[@id="comercial"]')

janela.close()

# texto do email vazio
texto_email = dolar_comercial + 'Hoje : ' + str(pd.Timestamp('today'))

# Email remetente , senha , destinatario
de = 'guilhermehernandezbatista@gmail.com'
senha = 'isxjkklremuywfyj'
destinatario = 'familiahernandez0123@gmail.com'

# montando mime
mensagem = MIMEMultipart()
mensagem['From'] = de
mensagem['To'] = destinatario
mensagem['Subject'] = 'Cotação do Dolar'

# Corpo do E-mail com anexos
mensagem.attach(MIMEText(texto_email, 'plain'))

# Criando sessão de SMTP para envio do E-mail
sessao = smtplib.SMTP('smtp.gmail.com', 587)  # Usuario gmail e porta
sessao.starttls()  # Habilita segurança
sessao.login(de, senha)  # Login de quem enviara o email

texto = mensagem.as_string()

sessao.sendmail(de, destinatario, texto)
sessao.quit()
