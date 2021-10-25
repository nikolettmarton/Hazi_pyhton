import random
kisbetu="qwertzuiopőúasdfghjkléáűíyxcvvbnm"
nagybetu=kisbetu.upper()
spec='\'''\\'
#print(spec)
print("Ez egy jelszó generáló program")
def kivesz(szoveg, darab):
    vissza=""
    for i in range(darab):
        vissza=vissza+szoveg[random.randrange(len(szoveg))]

    return vissza
print(kivesz(kisbetu,5))
print(kivesz(nagybetu,5))



