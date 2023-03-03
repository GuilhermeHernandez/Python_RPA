import pyautogui as p


#p.sleep(2)
#mov_google = p.position()
#print(mov_google)

p.doubleClick(x=35, y=526)  #Duplo click no navegador
p.sleep(4)

janela = p.getActiveWindow()    #Retorna pagina automatizada
janela.maximize()   #Mamixa pagina automatizada

p.write('www.udemy.com')    #Insere texto para pesquisa
p.press('enter')    #Comando enter
p.sleep(6)

indentificando_pesquisa = p.locateOnScreen('Pesquisa.PNG')   #Passando img para reconhecimento
local_pesquisa = p.center(indentificando_pesquisa)   #Passando centro da imagem

p.moveTo(local_pesquisa)    #Movendo mouse para centro da imagem
p.click(local_pesquisa)     #Clicando no centro da imagem
p.sleep(2)

p.write('RPA')      #Inserindo texto para pesquisa
p.press('enter')
p.sleep(5)

p.screenshot('Cursos RPA.png')
p.sleep(2)

indentificando_fechar = p.locateOnScreen('Close.PNG')   #Passando imagem para fechar
local_fechar = p.center(indentificando_fechar)  #Centro da imagem fecha

p.moveTo(local_fechar)#Movendo até fechar
p.click(local_fechar)
p.sleep(2)