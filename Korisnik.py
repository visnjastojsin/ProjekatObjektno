class Korisnik:

    def __init__(self, jmbg, ime, prezime, datum_rodjenja):
        self.__jmbg = jmbg
        self.__ime = ime
        self.__prezime = prezime
        self.__datum_rodjenja = datum_rodjenja


    @property
    def jmbg(self):
        return self.__jmbg

    @jmbg.setter
    def naziv(self, jmbg):
        self.__jmbg = jmbg

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def barkod(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def datum_rodjenja(self):
        return self.__datum_rodjenja

    @datum_rodjenja.setter
    def datum_rodjenja(self, datum_rodjenja):
        self.__datum_rodjenja = datum_rodjenja

    def __str__(self):
        format_linije = "{:>14}: {}"
        return "\n".join([
            "",
            format_linije.format(self.__jmbg),
            format_linije.format(self.__ime), format_linije.format(self.__prezime),
            format_linije.format(self.__datum_rodjenja)
        ])

    @classmethod
    def prikazi_korisnike(cls, korisnici):
        format_linije = "{:13} {:10} {:10} {:12}"

        print()
        # zaglavlje
        print(format_linije.format("JMBG", "Ime", "Prezime", "Datum rođenja"))
        print(format_linije.format("-" * 13, "-" * 10, "-" * 10, "-" * 12))
        # podaci
        for korisnik in korisnici:
            print(format_linije.format(
                korisnik.__jmbg,
                korisnik.__ime,
                korisnik.__prezime,
                korisnik.__datum_rodjenja
            ))

class Pacijent(Korisnik):

    def __init__(self, jmbg, ime, prezime, datum_rodjenja, LBO, recepti):
        super().__init__(jmbg, ime, prezime, datum_rodjenja)
        self.__LBO = LBO
        self.__recepti = recepti

    @property
    def LBO(self):
        return self.__LBO

    @LBO.setter
    def LBO(self, LBO):
        self.__LBO = LBO

    @property
    def recepti(self):
        return self.__recepti

    @recepti.setter
    def recepti(self, recepti):
        self.__recepti = recepti
    def __str__(self):
        format_linije = "{:>14}: {}"

        return "\n".join([
            super().__str__(),
            format_linije.format("LBO", self.__LBO)
                    ])

class Lekar(Korisnik):

    def __init__(self, jmbg, ime, prezime, datum_rodjenja, specijalizacija, recepti):
        super().__init__(jmbg, ime, prezime, datum_rodjenja)
        self.__specijalizacija = specijalizacija
        self.__recepti = recepti

    @property
    def specijalizacija(self):
        return self.__specijalizacija

    @specijalizacija.setter
    def specijalizacija(self, specijalizacija):
        self.__specijalizacija = specijalizacija

    @property
    def recepti(self):
        return self.__recepti

    @recepti.setter
    def recepti(self, recepti):
        self.__recepti = recepti

    def __str__(self):
        format_linije = "{:>14}: {}"

        return "\n".join([
            super().__str__(),
            format_linije.format("Specijalizacija", self.__specijalizacija)
        ])



