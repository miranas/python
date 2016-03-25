 #-*- coding: < UTF-8> -*-
stevilo = 4
vnos = int(raw_input("Vnesi stevilo:"))

if vnos < stevilo:
    print "premalo"
elif vnos == stevilo:
    print "Bingo!"
else:
    print "prevec"