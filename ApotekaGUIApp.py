from tkinter import *
from Korisnik import *
#from Podaci import Podaci
from tkinter import messagebox


def main():
    root = Tk()
    app = glavni_prozor(root)
    root.mainloop()


def ocisti_labele(self):
    self.__sifra_labela["text"] = ""
    self.__naziv_labela["text"] = ""
    self.__cena_labela["text"] = ""
    self.__proizvodjac_labela["text"] = ""




class glavni_prozor():

    def __init__(self, glavni):
        self.glavni = glavni

        self.glavni.title("Apoteka")
        self.glavni.geometry("1024x640")
        self.glavni.configure(bg="SkyBlue1")




        self.okvir = Frame(self.glavni)
        self.okvir.configure(bg="SkyBlue1")
        self.okvir.pack()


        self.labelTitle = Label(self.okvir,bd=10,relief = RIDGE, text="Apoteka",bg="SkyBlue1", fg="black", font=("Times New Roman", 35,"bold","italic"), padx = 2, pady=4)
        self.labelTitle.grid(row=2, column=1, sticky="")



        #kreiranje menija
        meni = Menu(glavni)
        glavni.config(menu=meni)

        izlaz_meni= Menu(meni)
        meni.add_cascade(label="Izlaz", menu=izlaz_meni)
        izlaz_meni.add_command(label="Izadji", command=self.glavni_izlaz)
        podaci_meni=Menu(meni)
        meni.add_cascade(label="Podaci", menu=podaci_meni)
        podaci_meni.add_command(label="Pacijenti",command = self.on_pacijenti)
        podaci_meni.add_separator()
        podaci_meni.add_command(label="Lekari", command=self.on_lekari)
        podaci_meni.add_separator()
        podaci_meni.add_command(label="Recepti", command=self.on_recepti)
        podaci_meni.add_separator()
        podaci_meni.add_command(label="Lekovi", command=self.on_lekovi)

    def glavni_izlaz(self):
        odgovor = messagebox.askokcancel("Exit", "Da li ste sigurni da želite da napustite aplikaciju?",
                                         icon="warning")
        if odgovor:
            self.destroy()


    def on_pacijenti(self):
        self.window = Toplevel(self.glavni)
        self.app = Prozor2(self.window)


    def on_lekari(self):
        window = Toplevel(self.glavni)
        window.title("Lekari")
        window.geometry("1024x640")

    def on_recepti(self):
        window = Toplevel(self.glavni)
        window.title("Recepti")
        window.geometry("1024x640")

    def on_lekovi(self):
        window = Toplevel(self.glavni)
        window.title("Lekovi")
        window.geometry("1024x640")



        #kreiranje dugmica
        #self.button1=Button(self.glavni, text="Pacijenti",height=2, width=20, font=("Times New Roman", 10,"bold","italic"))
        #self.button1.place(x=0, y=300, width=100)


        #self.button2 = Button(self.glavni, text="Lekari", height=2, width=20,font=("Times New Roman", 10, "bold", "italic"))
        #self.button2.place(x=100, y=300, width=100)
        #self.button3 = Button(self.glavni, text="Recepti", height=2, width=20,
#                              font=("Times New Roman", 10, "bold", "italic"))
        #self.button3.place(x=600, y=300, width=100)

        #self.button4 = Button(self.glavni, text="Lekovi", height=2, width=20,
           #                   font=("Times New Roman", 10, "bold", "italic"))
        #self.button4.place(x=850, y=300, width=100)

class Prozor2():

    def __init__(self, pacijent_prozor):
        self.pacijent_prozor = pacijent_prozor

        self.pacijent_prozor.title("Pacijenti")
        self.pacijent_prozor.geometry("1024x640")
        self.pacijent_prozor.configure(bg="SkyBlue1")

        self.okvir = Frame(self.pacijent_prozor)
        self.okvir.configure(bg="SkyBlue1")
        self.okvir.pack()

        self.labelTitle = Label(self.okvir, bd=10, relief=RIDGE, text="Pacijenti", bg="SkyBlue1", fg="black",
                                font=("Times New Roman", 35, "bold", "italic"), padx=2, pady=4)
        self.labelTitle.grid(row=2, column=1, sticky="")

if __name__ == "__main__":

    main()
