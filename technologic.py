import os
import time
import re
from random import randint

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

technologic = 'Buy it, use it, break it, fix it, Trash it, change it, melt - upgrade it, Charge it, pawn it, zoom it, press it, Snap it, work it, quick - erase it, Write it, cut it, paste it, save it, Load it, check it, quick - rewrite it, Plug it, play it, burn it, rip it, Drag and drop it, zip - unzip it, Lock it, fill it, curl it, find it, View it, coat it, jam - unlock it, Surf it, scroll it, pose it, click it, Cross it, crack it, twitch - update it, Name it, rate it, tune it, print it, Scan it, send it, fax - rename it, Touch it, bring it, pay it, watch it, Turn it, leave it, stop - format it.'

for index, item in enumerate(re.split('[,-]',technologic)): #separamos y recorremos el string (usamos enumerate para tener el indice del loop)
	cls() #limpiamos pantalla
	print '\n' * randint(1,10) + item.upper() #imprimimos en consola en una fila random y en mayusculas
	if index in [7, 15, 23, 30, 38, 46, 54, 62]: #nos fijamos si es final de frase
		time.sleep(0.5)
	else:
		time.sleep(0.3)
