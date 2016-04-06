# -*- encoding: utf-8 -*-
artikli = ["banane", "datlji", "pomarance", "slive"]
cena = [1.34, 2.45, 3.56, 4.67]

print artikli

izberi = raw_input("Izberi artikel:")


stevec = 0

if izberi in artikli:
    artikli_indexs = artikli.index(izberi)
    cena_artikla = cena[artikli_indexs]
    print "Cena artikla %s je: %s" %( izberi,cena_artikla)
    stevec += cena_artikla
    print "Tvoj racun znasa: " + str(stevec)
else:
    print "Tega izdelka ni med artikli v ponudbi"


znova = raw_input("Ce Zelis nadaljeveti nakupovanje vtipkaj da, ce zelis zakljuciti nakup vtipkaj karkoli")

while (znova == "da"):
    izberi = raw_input("Izberi artikel:")
    if izberi in artikli:
        artikli_indexs = artikli.index(izberi)
        cena_artikla = cena[artikli_indexs]
        print "Cena artikla %s znasa %s" % (izberi ,cena_artikla)
        stevec += cena_artikla
        print "Tvoj racun znasa: " + str(stevec)
        znova = raw_input("Ce Zelis nadaljeveti nakupovanje vtipkaj da, ce zelis zakljuciti nakup vtipkaj karkoli")

    else:
        print "Izbrani izdelek ni med artikli v ponudbi"
        print "Tvoj racun znasa: " + str(stevec)



print "Hvala za nakup. Tvoje plačilo znaša:  " + str(stevec)








