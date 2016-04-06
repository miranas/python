# -*- encoding: utf-8 -*-
artikli = ["banane", "datlji", "pomarance", "slive"]
cena = [1.34, 2.45, 3.56, 4.67]

print artikli  #da vidimo kaj imamo na razpolago

izberi = raw_input("Izberi artikel:")

stevec = 0


if izberi in artikli: #if zanka
    artikli_indexs = artikli.index(izberi) #smo se učili pri pouku, dobimo indeks od artikla v seznamu artikli.
    cena_artikla = cena[artikli_indexs] # in ga združimo s pripadajočo ceno iz seznama cena
    print "Cena artikla %s je: %s" %( izberi,cena_artikla)
    stevec += cena_artikla   #ceno artikla doda spremenljivki števec
    print "Tvoj racun znasa: " + str(stevec)
else:
    print "Tega izdelka ni med artikli v ponudbi"


znova = raw_input("Ce Zelis nadaljeveti nakupovanje vtipkaj da, ce zelis zakljuciti nakup vtipkaj karkoli")#tukaj se odločimo ali gremo v while zanko

while (znova == "da"):   #while zanka ponavlja vnos izberi dokler...
    izberi = raw_input("Izberi artikel:")
    if izberi in artikli:
        artikli_indexs = artikli.index(izberi)
        cena_artikla = cena[artikli_indexs]
        print "Cena artikla %s znasa %s" % (izberi ,cena_artikla)
        stevec += cena_artikla  #tale števec mora biti točno tu vmes, drugače ne dela
        print "Tvoj racun znasa: " + str(stevec)
        znova = raw_input("Ce Zelis nadaljeveti nakupovanje vtipkaj da, ce zelis zakljuciti nakup vtipkaj karkoli")  #možen izhod iz while zanke

    else:
        print "Izbrani izdelek ni med artikli v ponudbi" #če si se zatipkal dobiš račun in ponovno možnost 'izberi' v while zanki
        print "Tvoj racun znasa: " + str(stevec)



print "Hvala za nakup. Tvoje plačilo znaša:  " + str(stevec)  #tole se izvede, če izvršimo samo en nakup in ne gremo v while zanko








