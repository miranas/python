from ugani_drzavo import states

def povej_drzavo(drzava):
    return states[drzava]

def povej_mesto_in_drzavo(mesto,drzava):
    if povej_drzavo(drzava) == mesto:
        return "Bravo"
    else:
        return "Ouki douki"

def main():
    drzava = raw_input("Vnesi ime drzave: ")
    print povej_drzavo(drzava)

    drzava = raw_input("Povej drzavo:")
    mesto = raw_input("Povej glavno mesto: ")
    print povej_mesto_in_drzavo(mesto,drzava)


if __name__ == '__main__':
    main()
