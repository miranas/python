def sestevaj(st1,st2):
    rezultat = st1 + st2
    return int(rezultat)

def delez(mladina,prebivalci):
    rezultat = mladina / prebivalci * 100
    return format(rezultat, " .1f")


def main():
    st1 = int(raw_input("Vnesi stevilo 1: "))
    st2 = int(raw_input("Vnesi stevilo 2: "))
    print sestevaj(st1,st2)

    mladina = float(raw_input("Vnesi stevilo mladincev: "))
    prebivalci = float(raw_input("Vnesi stevilo vseh prebivalcev kraja:"))
    print delez(mladina, prebivalci)



if __name__ == "__main__":
    main()



