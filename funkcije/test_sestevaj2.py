from sestevaj import sestevaj
from sestevaj import delez


def test_sestevaj():
    assert sestevaj(2,3)==5
    assert sestevaj(3,4)==7
    return "Funkcija sestevaj() deluje pravilno."

print test_sestevaj()



def test_delez():
    assert delez(3, 4) == 75.0
    assert delez(100,1000) == 10.0
    return "Funkcija delez deluje"

print test_delez()


