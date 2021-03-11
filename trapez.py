import numpy as np
from math import sqrt

def funktion(x):
    return sqrt(1+x**3)
    #return sqrt(1+np.exp(2*x))

obere_Grenze = 1
untere_Grenze = 0

h = 12      #Anzahl der Intervalle 4 ist das Minimum das sinn macht!
sw = (obere_Grenze - untere_Grenze )/ h 

aktuellerwert = untere_Grenze
wertesammung = []
while aktuellerwert <= obere_Grenze:
    value = funktion(aktuellerwert)
    wertesammung.append(value)
    aktuellerwert = aktuellerwert + sw

endwert = wertesammung.pop()
startwert = wertesammung.pop(0)
zwischensumme = 0
for i in wertesammung:
    zwischensumme += i

#print(wertesammung)
result = (1/(2*h)) * (endwert + startwert + 2*zwischensumme)

print(result)
epsi = 0.001
#print(1/sqrt((epsi*12)/(np.exp(1))))