import rpa as r
import pyautogui as p

r.init()            #Permite rpa inicializar automação
r.url('https://www.google.com.br/')         #Navega até pagina informada !
r.wait(2.0)         #Espera em segundos informado

janela = p.getActiveWindow()
janela.maximize()

r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input','RPA[enter]')          #Interage com o elementos informado de acordo com seu parametro.


