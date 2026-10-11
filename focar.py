# FoCarilla liikkumiseen tarvittavat funktiot

def eteen(nopeus,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(aika)

def vasen(nopeus1,nopeus2,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus2)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(aika)

def oikea(nopeus1,nopeus2,aika):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus2)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(aika)

def kaannyAstetta(nopeus,aika):
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(aika)

def peruuta(nopeus,aika):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(aika)


# LED valon kontrollointi

