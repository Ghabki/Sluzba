from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Combobox

from Sluzba.Shranjevanje import *
from Sluzba.date_picker import *


# from Sluzba.main import *



class LoginFrame(Frame):
    shra = Shranjevanje()
    shra.register_file()




    def __init__(self, master):
        super().__init__(master)
        self.W = "300"
        self.H = "105"

        self.master.resizable(False, False)
        # to sem js dodau
        self.master.title("My work h app")
        self.master.geometry(self.W+"x"+self.H)
        self.center_window(int(self.W), int(self.H))

        self.master.iconbitmap(r"Resources\favicon.ico")

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")
        # string var za spreminjajoc se label
        self.besedilo = StringVar(self)
        self.update_label = Label(self.master, textvariable=self.besedilo)
        self.update_label.place(x=10, y=55)

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        # self.update_label.grid(row=3, sticky=E)
        # da fokusira okence
        self.entry_username.focus()

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=2, column=1, pady=2)

        self.regbtn = Button(self, text="Register", command=self._register_btn_clicked)
        self.regbtn.grid(row=3, column=1, pady=2)

        # master za enter, za gumb pa more bit posebej cene zazna tudi ozadje za klik
        self.master.bind("<Return>", self._login_btn_clicked)
        self.logbtn.bind("<Button-1>", self._login_btn_clicked)

        self.pack()

    # nekako lahko to dam v drugi class sam mi itak nerabi, jebiga je pac 2x isto napisano
    def center_window(self, w, h):
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def _register_btn_clicked(self):

        while True:
            username = self.entry_username.get()
            password = self.entry_password.get()

            self.shra.registracija(username, password)

            asciii = self.shra.get_ali_pravilen_ascii()
            space = self.shra.get_space()

            if space == 1:
                self.besedilo.set("Ime mora biti \n brez presledkov")
                break

            if asciii:
                rak = self.shra.get_x()
                if rak == 1:
                    self.besedilo.set("Že obstaja tak username")
                    break
                elif rak == 0:
                    self.besedilo.set("Registriran")
                    self.shra.create_new_folder_file(username)
                    break
                break
            else:
                self.besedilo.set("Uporabi samo ascii \n znake")
                break

    def _login_btn_clicked(self, event=None):
        # print("Clicked")
        print("pressed")
        while True:
            username = self.entry_username.get()
            password = self.entry_password.get()

            if self.shra.prijava(username, password):
                set_username(self, username)
                # NEVEM KAKO TO DELA NEVEM ZAKAJ TO DELA NEVEM ZAKAJ JE TO TAKO RAKAVO!!
                self.master.withdraw()
                self.glavno_okno = Toplevel(self.master)
                MainScreen(self.glavno_okno, username)
                break
            else:
                self.besedilo.set("Napačni username \n ali geslo")
                break


class MainScreen(Frame, ):
    shra = Shranjevanje()
    def __init__(self, master, glavno_ime):
        super().__init__(master)
        self.W = "650"
        self.H = "345"

        # magic iz prejsnjega classa ko se poklice ka class enostavno potrebuje da se noter da ime
        self.glavno_ime = glavno_ime

        self.master.resizable(False, False)
        self.master.title("My work hour app")
        self.master.geometry(self.W+"x"+self.H)
        # self.center_window(int(self.W), int(self.H))

        self.master.iconbitmap(r"Resources\favicon.ico")
        self.master.configure(background='gray14')

        # overrida kar naredi X button pri oknu
        self.master.protocol("WM_DELETE_WINDOW", self.exit_fix)

        self.frame = Frame(self.master, width=345, background="steel blue")
        self.frame.pack(fill=X)

        self.values_evri = []
        self.vrednosti = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0]
        self.meseci = ["Januar", "Februar", "Marec", "April", "Maj", "Junij", "Julij", "August","September","Oktober", "November", "December"]
        self.leta = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028"]
        self.za_evre()

        self.checkbox_izbira = Tkinter.IntVar()
# ----------------------------------------------------------------------------------------------------------------------
        # naredi listbox
        self.create_list_box()
# ----------------------------------------------------------------------------------------------------------------------
        # naredi lable da lahko izbereš datum
        self.izbira_datuma = Label(self.frame, text="Pričetek dela", bg="steel blue")
        self.izbira_datuma.place(x=300, y=20)

        self.datum_window = Datepicker(self.frame)
        self.datum_window.place(x=380, y=20)
# ----------------------------------------------------------------------------------------------------------------------

        # naredi check button da si zapomne izbire za ta username
        self.zapomni_izbiro = Checkbutton(self.frame, text="Zapomni si izbire", bg="steel blue", activebackground="steel blue")
        self.zapomni_izbiro.place(x=530, y=18)
# ----------------------------------------------------------------------------------------------------------------------

        # naredi check box za to da ce zelis imeti fixne ure ali dnevne pa nocne
        self.izberi_DanNoc = Checkbutton(self.frame, text="Izbira dnevna in nočna", bg="steel blue",
                                          activebackground="steel blue", variable=self.checkbox_izbira)
        self.izberi_DanNoc.place(x=320, y=50)
# ----------------------------------------------------------------------------------------------------------------------


        # naredi combo box za izbiro denarja na uro za dan

        self.dan = Label(self.frame, text="Dnevni denar", bg="steel blue")
        self.dan.place(x=300, y=80)
        self.ure_dan = ttk.Combobox(self.frame, values=self.values_evri, width=10)
        self.ure_dan.place(x=380, y=80)
        self.ure_dan.current(87)  # <------------------------- todo uporabi to za nastaviti željeno vrednost ob prijavi

        # evri_ure['values'] = ('USA', 'Canada', 'Australia')
        # naredi combo box za nocne ure
        self.noc = Label(self.frame, text="Nocni denar", bg="steel blue")
        self.noc.place(x=470, y=80)
        self.ure_nocna = ttk.Combobox(self.frame, values=self.values_evri, width=10)
        self.ure_nocna.place(x=543, y=80)
        self.ure_nocna.current(187)

        # to je za ure pri dnevno nocnih vrednosti
        self.dan_denar = Label(self.frame, text="Št. dnevnih ur", bg="steel blue")
        self.dan_denar.place(x=300, y=110)
        self.denar_dan = ttk.Combobox(self.frame, values=self.vrednosti, width=10)
        self.denar_dan.place(x=380, y=110)

        self.noc_denar = Label(self.frame, text="Št. nočnih ur", bg="steel blue")
        self.noc_denar.place(x=470, y=110)
        self.denar_noc = ttk.Combobox(self.frame, values=self.vrednosti, width=10)
        self.denar_noc.place(x=543, y=110)
# ----------------------------------------------------------------------------------------------------------------------

        # okno za fixne ure
        self.fixno = Label(self.frame, text="Fixni denar", bg="steel blue")
        self.fixno.place(x=300, y=140)
        self.fixne_denar = ttk.Combobox(self.frame, values=self.values_evri, width=10)
        self.fixne_denar.place(x=380, y=140)

        self.fixno = Label(self.frame, text="Fixne ure", bg="steel blue")
        self.fixno.place(x=470, y=140)
        self.fixne_ure = ttk.Combobox(self.frame, values=self.vrednosti, width=10)
        self.fixne_ure.place(x=543, y=140)
# ----------------------------------------------------------------------------------------------------------------------

        # dodajanje v listbox gumb
        self.add_button = Button(self.frame, text="Dodaj", command=self.dodaj_delo)
        self.add_button.place(x=380, y=172)
        self.add_button.config(height=1, width=16)
# ----------------------------------------------------------------------------------------------------------------------

        # izberi mesec in letoza izračun
        self.Izracun_meseci = Label(self.frame, text="Izračun: \nmesec-leto", bg="steel blue")
        self.Izracun_meseci.place(x=300, y=202)

        self.mesec = ttk.Combobox(self.frame, values=self.meseci, width=10)
        self.mesec.place(x=380, y=209)
        self.leto = ttk.Combobox(self.frame, values=self.leta, width=10)
        self.leto.place(x=470, y=209)

        self.delbtn = Button(self.frame, text="Izracun", command=self.delete)  # todo nepozabi spremeniti tele funkcije
        self.delbtn.place(x=580, y=208)

        # izpis plače
        self.Izracun_meseci = Label(self.frame, text="Plača: ", bg="steel blue")
        self.Izracun_meseci.place(x=300, y=250)
        self.placa = StringVar(self)  # <---------------
        self.update_label_placa = Label(self.frame, textvariable=self.placa)
        self.update_label_placa.place(x=400, y=250)

# ----------------------------------------------------------------------------------------------------------------------

        # izpis napak
        self.napaka = StringVar(self)  # <---------------
        # self.napaka.set("sdth")

        self.update_label_napaka = Label(self.frame, textvariable=self.napaka, bg="steel blue")
        self.update_label_napaka.place(x=300, y=300)


# ----------------------------------------------------------------------------------------------------------------------
        # gumb za izbrista vrstico iz listboxa
        self.delbtn = Button(self.frame, text="Delete", command=self.delete)
        self.delbtn.place(x=580, y=300)
# ----------------------------------------------------------------------------------------------------------------------



    def center_window(self, w, h):
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def za_evre(self):
        a = 4.12
        for i in range(0, 250):
            a = a + 0.01
            a = round(a, 2)
            self.values_evri.insert(i, a)
        print(self.values_evri)

    @staticmethod
    def exit_fix():
        print("destroyed")
        root.destroy()

    def create_list_box(self):
        listbox = Listbox(self.frame, height=21, width=30, selectmode=SINGLE, font="14")
        scroll = Scrollbar(self.frame, command=listbox.yview)

        listbox.configure(yscrollcommand=scroll.set)
        listbox.pack(side=LEFT, fill=Y)
        scroll.pack(side=LEFT, fill=Y)
        # todo tukaj pride vrjetno koda za izpis iz datoteke
        for item in range(30):
            listbox.insert(END, item)




    def lolek(self):
        # a = self.Datepicker.get()
        print("fdshgsghdf")
        print(self.datum_window.current_text)

    def dodaj_delo(self):

        self.shra.create_new_folder_file(self.glavno_ime)
        # datoteka.write(name + "\n")
        datoteka = open("Profile_data/" + self.glavno_ime + ".txt", "a")

        if self.checkbox_izbira.get() == 1:
            datum = self.datum_window.get()
            day_ure = self.ure_dan.get()
            day_mony = self.denar_dan.get()
            night_ure = self.ure_nocna.get()
            night_mony = self.denar_noc.get()

            if datum == "" or day_ure == "" or day_mony == "" or night_ure == "" or night_mony == "":
                self.napaka.set("Prazno polje!!!")
                print("pratno polje")
            else:
                datoteka.write(datum + " " + day_ure + " " + day_mony + " " + night_ure + " " + night_mony + "\n")
                print("napisano v file")
                self.napaka.set("Shranjeno v file")
        else:
            datum = self.datum_window.get()
            ure = self.fixne_ure.get()
            denar_fix = self.fixne_denar.get()

            if datum == "" or ure == "" or denar_fix == "":
                self.napaka.set("Prazno polje!!!")
                print("prazno polje")
            else:
                datoteka.write(datum + " " + ure + " " + denar_fix + "\n")
                print("napisano v file")
                self.napaka.set("Shranjeno v file")

            print(datum+" "+ure+" "+denar_fix)
        datoteka.close()

    def delete(self):
        #koda za izbris necesa v filu
        print("delete")
        # window = Toplevel(root)


if __name__ == '__main__':
    root = Tk()
    prvo_okno = LoginFrame(root)

    root.mainloop()
