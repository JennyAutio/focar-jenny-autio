from machine import Pin, PWM
from time import sleep

# Nopeus 100% = 65534
# Nopeus 75% = 49150
# Nopeus 50% = 32767
# Nopeus 25% = 16384

n100=65534
n75=49150
n50=32767
n25=16384
n=0
tauko=1


from focar import eteen
from focar import oikea
from focar import peruuta
from focar import lopeta
from focar import kaannyAstetta
from focar import vilkutaLED


sleep(5)
eteen(n50,5)
oikea(n25,n100,2)
peruuta(n50,3)
kaannyAstetta(n50,2)
eteen(n100,tauko)
vilkutaLED(2)
lopeta()