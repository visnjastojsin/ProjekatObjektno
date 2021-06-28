from Korisnik import Pacijent
from Korisnik import Lekar
from Lek import Lek

class Recept:

    @property
    def pacijent(self):
        return Pacijent

    @pacijent.setter
    def pacijent(self,pacijent):
        self.__pacijent = pacijent

    def __init__(self, pacijent, datum_i_vreme, izvestaj, lekar, lek, kolicina):

        self.__pacijent = pacijent
        self.__datum_i_vreme = datum_i_vreme
        self.__izvestaj = izvestaj
        self.__lekar = lekar
        self.__lek = lek

    @property
    def lekar(self):
        return Lekar

    @lekar.setter
    def lekart(self, lekar):
        self.__lekar = lekar

    @property
    def lek(self):
        return Lek

    @lek.setter
    def lek(self, lek):
        self.__lek = lek

    @property
    def datum_i_vreme(self):
        return self.__datum_i_vreme

    @datum_i_vreme.setter
    def datum_i_vreme(self, datum_i_vreme):
        self.__datum_i_vreme = datum_i_vreme

    @property
    def kolicina(self):
        return self.__kolicina

    @kolicina.setter
    def kolicina(self, kolicina):
        self.__kolicina = kolicina

    def __str__(self):
        format_linije ="{:13} {:10} {:10} {:12}"

        return "\n".join([
            format_linije.format("Pacijent:", self.__pacijent),
            format_linije.format("Datum i vreme: ", self.__datum_i_vreme),
            format_linije.format("Izvestaj: ", self.__izvestaj),
            format_linije.format("Lekar: ", self.__lekar),
            format_linije.format("Lek: ", self.__lek),
            format_linije.format("Kolicina: ", self.__kolicina)
        ])