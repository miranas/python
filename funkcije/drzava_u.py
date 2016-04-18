podatki = {
    "Slovenija":"Ljubljana",
    "Avstrija":"Dunaj",
    "Italija":"Rim"
}

def izpisi_gl_mesto(drzava):
    return podatki[drzava]

def izpisi_drzavo(mesto):
    for drzava in podatki.keys():
          if (mesto == podatki[drzava]):
              return drzava
          # else namenoma manjka (da gre zanka naprej)
    return "Nisem nasel :)"

def preveri(mesto, drzava):
    pravilno_mesto = izpisi_gl_mesto(drzava)
    return mesto == pravilno_mesto

def izpisi_vse():
    print podatki

if __name__ == "__main__":
    izpisi_vse()
    stevilka = 4
    print podatki.keys()
    for drzava in podatki.keys():
        a = 3
        while a != 0:

            drzava1 = izpisi_drzavo(mesto)
            print "D: {}".format(drzava1)
            pravilno = preveri(mesto, drzava)
            if pravilno:
                print "Pravilno"
                break
            else:
                print "Narobe"
                a -= 1