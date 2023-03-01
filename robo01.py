import pyautogui as p

p.hotkey('win','r')
p.sleep(1)

p.typewrite('notepad')
p.sleep(1)

p.press('enter')
p.sleep(1)

p.typewrite('Ola , sou um bot !')
p.sleep(1)

janela = p.getActiveWindow()
janela.close()
p.sleep(1)

p.press('right')
p.sleep(1)
p.press('enter')