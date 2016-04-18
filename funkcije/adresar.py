
class Kontakt:
    def __init__(self,ime,priimek,naslov,email,telefon):
        self.ime = ime
        self.priimek = priimek
        self.naslov = naslov
        self.email = email
        self.telefon = telefon

    def ime_in_priimek(self):
        return self.ime, self.priimek

seznam = []

while True:
    odgovor = raw_input("Zelis vnesti nov kontakt y/n")

    if odgovor == "y":

        vnos = Kontakt(ime="", priimek="", naslov="", email="", telefon="")

        vnos.ime = raw_input("Povej ime:")
        vnos.priimek = raw_input("Povej priimek:")
        vnos.naslov = raw_input("Povej naslov:")
        vnos.email = raw_input("Povej email:")
        vnos.telefon = raw_input("Povej telefon:")


    else:
        break


print vnos.ime
print vnos.priimek
print vnos.ime_in_priimek()










