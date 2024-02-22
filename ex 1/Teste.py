from Funcionalidades import *

tv = Televisor('Panasonic','Panasonic XYZ')

controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)

controle.sintonizaCanal('Globo')
controle.trocaCanal('Globo')

print(tv.canal_atual)

print(tv.volume)

controle.aumentaVolume()

print(tv.volume)