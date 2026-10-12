from machine import Pin, PWM
from time import sleep

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

#  Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# FoCarilla liikkumiseen tarvittavat funktiot

# tätä funktiota kutsuttaessa mennään eteenpäin määritetty aika
def eteen(nopeus,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

# tätä funktiota kutsuttaessa käännytään vasemmalle
def vasen(nopeus1,nopeus2,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus2)
    sleep(aika)

# tätä funktiota kutsuttaessa käännytään oikealle
def oikea(nopeus1,nopeus2,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus2)
    sleep(aika)

# tätä funktiota kutsuttaessa käännytään paikallaan esim. puoliympyrä tai ympyrä
def kaannyAstetta(nopeus,aika):
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

# tätä funktiota kutsuttaessa peruutetaan
def peruuta(nopeus,aika):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

# tämä funktio kutsutaan, kun reitti on valmis
def lopeta():
    sleep(1)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)



# LED valon kontrollointi

led=Pin("LED", Pin.OUT)

def vilkutaLED():
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

