from machine import Pin, PWM

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

#  Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)


# Nopeus 100% = 65534
# Nopeus 75% = 49150
# Nopeus 50% = 32767
# Nopeus 25% = 16384
