states = {
    "Slovenija":"Ljubljana",
    "Avstrija":"Dunaj",
    "Italija":"Rim",
    "Francija":"Pariz"
}
def povej_mesto(mesto):
    return states[mesto]

def main():

    stevec = 0

    for x in states.keys():
        mesto = raw_input("Vnesi glavno mesto drzave " + x + ":")
        if states[x] == mesto:
            stevec += 1
            print "Bingo!"
        else:
            print "Slabo"
            print "Pravilen odgovor je " + povej_mesto(x)


    print "Stevilo dosezenih tock je: {}".format(stevec)



if __name__ == '__main__':
    main()