from random import randint

a = []  #definiramo dve listi a in b
b = []

def odstrani_dvojnike(a):
    for x in a: #preglej vsa stevila, ki jih imas v listi a
        if x not in b:  #Vsa stevila, x, ki so v listi a, ni pa jih SE v  listi b..
            b.append(x) #...dodaj listi b. V listo b gre zato iz liste a samo po eno enako stevilo
    return b  #funkcija vrne napolnjeno listo b

def printaj():
    while(len(b)) < 8:  #dokler se lista b(preko liste a) ne napolni z osmimi neenakimi stevili...
        a.append(randint(1,39)) #..generiraj nakljucna stevila od 0 do 9 in jih filaj v listo a
        if len(odstrani_dvojnike(a))== 8: #printaj mi samo tisto verzijo liste b, ki je napolnjena z osmimi stevili
            print odstrani_dvojnike(a) #funkcija, ki vrne listo b,definirana zgoraj


print printaj()
