#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
container = 0

genetika = open("dna.txt", "r").read()


spol_m = genetika.find("TGCAGGAACTTC")
if spol_m  > -1:
    dokaz1 = True
    print "Osumljenec je moskega spola"
else:
    dokaz1 = False



spol_z = genetika.find("TGAAGGACCTTC")
if spol_z > -1:
    dokaz2 = True
    print "Osumljenec je zenskega spola"
else:
    dokaz2 = False



rasa_b = genetika.find("AAAACCTCA")
if rasa_b > -1:
    dokaz3 = True
    print "Osumljenec je belec."
else:
    dokaz3 = False



rasa_c = genetika.find("CGACTACAG")
if rasa_c > -1:
    dokaz4 = True
    print "Osumljenec je crnec."
else:
    dokaz4 = False



rasa_a = genetika.find("CGCGGGCCG")
if rasa_a > -1:
    dokaz5 = True
    print "Osumljenec je azijat"
else:
    dokaz5 = False


oci_modra = genetika.find("TTGTGGTGGC")
if oci_modra > -1:
    dokaz6 = True
    print "Osumljenec je modrook."
else:
    dokaz6 = False


oci_zelena = genetika.find("GGGAGGTGGC")
if oci_zelena > -1:
    dokaz7 = True
    print "Osumljenec je zelenook."
else:
    dokaz7 = False


oci_rjava = genetika.find("AAGTAGTGAC")
if oci_rjava > -1:
    dokaz8 = True
    print "Osumljenc je rjavook"
else:
    dokaz8 = False



obraz_kvadrat = genetika.find("GCCACGG")
if obraz_kvadrat > -1:
    dokaz9 = True
    print "Osumljenec ima kvadraten obraz"
else:
    dokaz9 = False



obraz_okrogel = genetika.find("ACCACAA")
if obraz_okrogel > -1:
    dokaz10 = True
    print "Osumljenec ima okrogel obraz"
else:
    dokaz10 = False


obraz_oval = genetika.find("AGGCCTCA")
if obraz_oval > -1:
    dokaz11 = True
    print "Osumljenec ima ovalen obraz"
else:
    dokaz11 = False


lasje_crni = genetika.find("CCAGCAATCGC")
if lasje_crni > -1:
    dokaz12 = True
    print "Osumljenec je crnolas"
else:
    dokaz12 = False



lasje_rjavi = genetika.find("GCCAGTGCCG")
if lasje_rjavi > -1:
    dokaz13 = True
    print "Osumljenec je rjavolas"
else:
    dokaz13 = False


lasje_rusi = genetika.find("TTAGCTATCGC")
if lasje_rusi > -1:
    dokaz14 = True
    print "Osumljenec je rusolas"
else:
    dokaz14 = False




ime = raw_input("Vnesi Ime osumljenca:")



spol = raw_input("vnesi spol osumljenca: 1 = male, 2 = female")

if spol == "1":
    if dokaz1 == True:
        container += 1
    else:
        print "Spol ne ustreza"

elif spol == "2":
    if dokaz2 == True:
        container += 1
    else:
        print "Spol ne ustreza"

else:
    print "Spol ne ustreza"



rasa = raw_input("vnesi raso osumljenca: 1 = belec, 2 = crnac 3 = azijat")

if rasa == "1":
    if dokaz3 == True:
        container += 1
    else:
        print "Rasa ne ustreza"

elif rasa == "2":
    if dokaz4 ==True:
        container += 1
    else:
        print "Rasa ne ustreza"

elif rasa == "3":
    if dokaz5 == True:
        container += 1
    else:
        print "Rasa ne ustreza"

else:
    print "Rasa ne ustreza"





oko = raw_input("vnesi barvo oci osumljenca: 1 = modra, 2 = zelena 3 = rjava")

if oko == "1":
    if dokaz6 == True:
        container = container + 1
    else:
        print "Barva o?i ne ustreza"


elif oko == "2":
    if dokaz7 == True:
        container = container + 1
    else:
        print "Barva o?i ne ustreza"


elif oko == "3":
    if dokaz8 == True:
        container = container + 1
    else:
        print "Barva o?i ne ustreza"

else:
    print "Barva o?i ne ustreza"




obraz = raw_input("vnesi obliko obraza osumljenca: 1 = kvadrat, 2 = okrogel 3 = oval")

if obraz == "1":
    if dokaz9 == True:
        container += 1
    else:
        print "Obraz ne ustreza"

elif obraz == "2":
    if dokaz10 == True:
        container += 1
    else:
        print "Obraz ne ustreza"

elif obraz == "3":
    if dokaz11 == True:
        container += 1
    else:
        print "Obraz ne ustreza"

else:
    print "obraz ne ustreza"



lasje = raw_input("vnesi barvo las osumljenca: 1 = crni, 2 = rjavi 3 = rusi")

if lasje == "1":
    if dokaz12 == True:
        container += 1
    else:
        print "Barva las ne ustreza"

elif lasje == "2":
    if dokaz13 == True:
        container += 1
    else:
        print "Barva las ne ustreza"

elif lasje == "3":
    if dokaz14 == True:
        container += 1
    else:
        print "Barva las ne ustreza"

else:
    print "Barva las  ne ustreza"



if container == 5:
    print "Hop cefizelj!"
else:
    print "Osumljenec " + ime +" ni kriv"
    print "Ustreza  v " + str(container) + "  od 5-ih lastnosti"



























