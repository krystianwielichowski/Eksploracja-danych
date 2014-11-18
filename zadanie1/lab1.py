# Wzorowane na przyk³adzie Rona Zacharskiego
#
from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
        "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
        "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
        "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
        "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
        "Fruzia": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
        "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
        "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}
def manhattan(rating1, rating2):
    """Oblicz odleg³oœæ w metryce taksówkowej miêdzy dwoma zbiorami ocen
    danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
    Zwróæ -1, gdy zbiory nie maj¹ wspólnych elementów"""
    # TODO: wpisz kod
    # kl = rating1.keys()

    zespoly1 = rating1.keys()
    oceny1 = rating1.values()

    zespoly2 = rating2.keys()
    oceny2 = rating2.values()

    odleglosc = 0
    udaloSiePorownac = False

    for zespol in zespoly1:
        if zespol in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[zespol] - rating1[zespol])
        pass
    if udaloSiePorownac:
        return odleglosc
    else:
        return -1

def testManhattan(rating1, rating2, odleglosc):
    if manhattan(rating1, rating2) == odleglosc:
        return True
    else:
        return False
    

def obliczNajblizszegoSasiada(uzytkownik, uzytkownicy):
    """dla danego u¿ytkownika, zwróæ listê innych u¿ytkowników wed³ug bliskoœci preferencji"""
    odleglosci = []
    
    
    for porownywanyUzytkownik in uzytkownicy:
        odleglosc = 0
        if uzytkownik != porownywanyUzytkownik:
            odleglosc = manhattan(uzytkownicy[uzytkownik], uzytkownicy[porownywanyUzytkownik])
            odleglosci.append((odleglosc, porownywanyUzytkownik))
    return sorted(odleglosci)


def recommend(username, users):
    """Zwróæ listê rekomendacji dla u¿ytkownika"""
    # znajdŸ preferencje najbli¿szego s¹siada
    nearest = obliczNajblizszegoSasiada(username, users)[0][1]
    recommendations = []
    ratingOfNearest = users[nearest]
    userRating = users[username]

    for artist in ratingOfNearest:
        if not artist in userRating:
            recommendations.append((artist, ratingOfNearest[artist]))
        
    # zarekomenduj u¿ytkownikowi wykonawcê, którego jeszcze nie oceni³, a zrobi³ to jego najbli¿szy s¹siada
    # TODO: wpisz kod
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

# przyk³ady
print 'Najbli¿szy s¹siad: %s' % obliczNajblizszegoSasiada('Hela', users)[0][1]
print( recommend('Hela', users))

print( recommend('Celina', users))

odleglosc = manhattan(users["Ania"], users["Hela"])
print ("Od Ani do Heli jest %2.1f" % odleglosc)
print testManhattan({'³zy':5, 'TL':3},
                    {'³zy':10},
                    5
    )
print obliczNajblizszegoSasiada('Hela', users)
