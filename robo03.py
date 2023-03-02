import rpa as r
import pyautogui as p

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
r.wait(2.0)

janela = p.getActiveWindow()
janela.maximize()

dolar_comercial = r.read('//*[@id="comercial"]')

janela.close()
