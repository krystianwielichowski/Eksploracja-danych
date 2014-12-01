#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt
from numpy import corrcoef

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2.0,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    korelacja=0
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    x=[]
    y=[]
    
    for klucz1 in klucze1:
         for klucz2 in klucze2:
             if (klucz1 == klucz2):
                 x.append(rating1[klucz1])
                 y.append(rating2[klucz2])
    
    sumaX=0
    sumaX2=0
    sumaY=0
    sumaY2=0
    sumaXY=0
       
    n= len(x)
    for i in xrange(0, n):
        sumaX += x[i]
        sumaX2 += x[i] ** 2
        sumaY += y[i]
        sumaY2 += y[i] ** 2
        sumaXY += x[i] * y[i]
    
    korelacja = (sumaXY - sumaX * sumaY / n) / (sqrt(sumaX2 - sumaX ** 2 / n) * (sqrt(sumaY2 - sumaY ** 2 / n)))
    return korelacja

def pearsonNumpy(rating1, rating2):
    
    korelacja=0
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    x=[]
    y=[]
    
    for klucz1 in klucze1:
         for klucz2 in klucze2:
             if (klucz1 == klucz2):
                 x.append(rating1[klucz1])
                 y.append(rating2[klucz2])

    korelacja = corrcoef(x, y)[0,1]
    return korelacja

print pearson(users["Ania"], users["Bonia"])
print pearsonNumpy(users["Ania"], users["Bonia"])

