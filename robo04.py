import pyautogui as p


#p.sleep(2)
#mov_google = p.position()
#print(mov_google)

p.doubleClick(x=35, y=526)
p.sleep(4)

janela = p.getActiveWindow()
janela.maximize()

p.write('www.udemy.com')
p.press('enter')
p.sleep(6)

indetificando_pesquisa = p.locateOnScreen('Pesquisa.PNG')   #Passando img para reconhecimento
local_pesquisa = p.center(indetificando_pesquisa)   #Passando centro da imagem

p.moveTo(local_pesquisa, duration=1)
p.click(local_pesquisa)
p.sleep(2)

p.write('RPA')
p.press('enter')
p.sleep(2)
