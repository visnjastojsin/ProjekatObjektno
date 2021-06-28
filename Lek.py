class Lek:

    def __init__(self, JLK, naziv, proizvodjac, tip_leka, recepti):
        self.__JLK = JLK
        self.__naziv = naziv
        self.__proizvodjac = proizvodjac
        self.__tip_leka = tip_leka
        self.__recepti = recepti


    @property
    def JLK(self):
        return self.__JLK

    @JLK.setter
    def JLK(self, JLK):
        self.__JLK = JLK

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    @property
    def proizvodjac(self):
        return self.__proizvodjac

    @proizvodjac.setter
    def proizvodjac(self, proizvodjac):
        self.__proizvodjac = proizvodjac

    @property
    def tip_leka(self):
        return self.__tip_leka

    @tip_leka.setter
    def tip_leka(self, tip_leka):
        self.__tip_leka = tip_leka
    @property
    def recepti(self):
        return self.__recepti

    @recepti.setter
    def recepti(self, recepti):
        self.__recepti = recepti

    def __str__(self):
        format_linije ="{:13} {:10} {:10} {:12}"

        return "\n".join([
            format_linije.format("JKL:", self.__JLK),
            format_linije.format("Naziv: ", self.__naziv),
            format_linije.format("Tip Leka: ", self.__tip_leka),
            format_linije.format("Proizvodjac: ", self.__proizvodjac)
        ])