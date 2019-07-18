#uredi import. Nerabi vsega importat...
from tkinter import *
from tkinter.ttk import Combobox

from Shranjevanje import *
from date_picker import *


class LoginFrame(Frame):
    shra = Shranjevanje()
    shra.register_file()

    def __init__(self, master):
        super().__init__(master)
        self.W = "300"
        self.H = "105"

        self.master.resizable(False, False)
        # to sem js dodau
        self.master.title("Hourglass")
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
                self.besedilo.set("Name should not \n contain whitespaces")
                break

            if asciii:
                rak = self.shra.get_x()
                if rak == 1:
                    self.besedilo.set("Name already exists")
                    break
                elif rak == 0:
                    self.besedilo.set("Registered")
                    self.shra.create_new_folder_file(username)
                    break
                break
            else:
                self.besedilo.set("Use only ascii \n characters")
                break

    def _login_btn_clicked(self, event=None):
        # print("Clicked")
        print("login_btn pressed")
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
                self.besedilo.set("Wrong username  \n or password")
                break


class MainScreen(Frame):
    shra = Shranjevanje()

    def __init__(self, master, glavno_ime):
        super().__init__(master)
        self.W = "660"
        self.H = "345"

        # magic iz prejsnjega classa ko se poklice ka class enostavno potrebuje da se noter da ime
        self.glavno_ime = glavno_ime

        self.master.resizable(False, False)
        self.master.title("Hourglass")
        self.master.geometry(self.W+"x"+self.H)
        # self.center_window(int(self.W), int(self.H))

        self.master.iconbitmap(r"Resources\favicon.ico")
        self.master.configure(background="gray14")

        # overrida kar naredi X button pri oknu
        self.master.protocol("WM_DELETE_WINDOW", self.exit_fix)

        self.frame = Frame(self.master, width=345, background="steel blue")
        self.frame.pack(fill=X)

        self.values_evri = []
        self.meseci_dic = {"January": "01", "February": "02","March": "03","April": "04","May": "05","June": "06",
                    "July": "07","August": "08","September": "09","October": "10","November": "11","December": "12",}
        self.vrednosti = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0]
        self.meseci = ["January", "February", "March", "April", "May", "June", "July", "August","September","October", "November", "December"]
        self.leta = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028"]
        self.labelfont = ("calibri", 12, 'bold')
        self.velikost = ("calibri", 13, 'bold')
        self.za_evre()

        self.checkbox_izbira = IntVar()
        self.checkbox_izbira_dva = IntVar()
# ----------------------------------------------------------------------------------------------------------------------
        # naredi listbox
        self.create_list_box()
# ----------------------------------------------------------------------------------------------------------------------
        # naredi lable da lahko izbereš datum
        self.izbira_datuma = Label(self.frame, text="Date", bg="steel blue")
        self.izbira_datuma.place(x=315, y=20)

        self.datum_window = Datepicker(self.frame)
        self.datum_window.place(x=395, y=20)
# ----------------------------------------------------------------------------------------------------------------------

        # naredi check button da si zapomne izbire za ta username
        self.zapomni_izbiro = Checkbutton(self.frame, text="Remember", bg="steel blue", activebackground="steel blue")
        self.zapomni_izbiro.place(x=540, y=18)
# ----------------------------------------------------------------------------------------------------------------------

        # naredi check box za to da ce zelis imeti fixne ure ali dnevne pa nocne
        self.izberi_DanNoc = Checkbutton(self.frame, text="Day/Night €/h", bg="steel blue",
                                          activebackground="steel blue", variable=self.checkbox_izbira, command=self.dan_noc_ena_des)
        self.izberi_DanNoc.place(x=375, y=50)

        self.izberi_Fixno = Checkbutton(self.frame, text="Fixed €/h", bg="steel blue",
                                          activebackground="steel blue", variable=self.checkbox_izbira_dva, command=self.fixno_ena_des)
        self.izberi_Fixno.place(x=540, y=50)

# ----------------------------------------------------------------------------------------------------------------------
        self.noc_ure = Label(self.frame, text="I I", bg="steel blue", font=self.velikost)
        self.noc_ure.place(x=428, y=93)

        self.noc_ure = Label(self.frame, text="I I", bg="steel blue", font=self.velikost)
        self.noc_ure.place(x=590, y=93)
        # ----------------------------------------------------------------------------------------------------------------------

        # naredi combo box za izbiro denarja na uro za dan

        self.dan = Label(self.frame, text="Day money", bg="steel blue")
        self.dan.place(x=315, y=80)
        self.denar_dan = ttk.Combobox(self.frame, values=self.values_evri, width=10)
        self.denar_dan.place(x=395, y=80)
        self.denar_dan.current(87)  # <------------------------- todo uporabi to za nastaviti željeno vrednost ob prijavi

        # evri_ure['values'] = ('USA', 'Canada', 'Australia')
        # naredi combo box za nocne ure
        self.noc = Label(self.frame, text="Night money", bg="steel blue")
        self.noc.place(x=485, y=80)
        self.denar_noc = ttk.Combobox(self.frame, values=self.values_evri, width=10)
        self.denar_noc.place(x=558, y=80)
        self.denar_noc.current(187)

        # to je za ure pri dnevno nocnih vrednosti
        self.dan_ure = Label(self.frame, text="Day hours", bg="steel blue")
        self.dan_ure.place(x=315, y=110)
        self.ure_dan = ttk.Combobox(self.frame, values=self.vrednosti, width=10)
        self.ure_dan.place(x=395, y=110)

        self.noc_ure = Label(self.frame, text="Night hours", bg="steel blue")
        self.noc_ure.place(x=485, y=110)
        self.ure_noc = ttk.Combobox(self.frame, values=self.vrednosti, width=10)
        self.ure_noc.place(x=558, y=110)
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

        # okno za fixne ure
        self.fixno = Label(self.frame, text="Fixed money", bg="steel blue")
        self.fixno.place(x=315, y=140)
        self.fixne_denar = ttk.Combobox(self.frame, values=self.values_evri, width=10)
        self.fixne_denar.place(x=395, y=140)

        self.fixno = Label(self.frame, text="Fixed time", bg="steel blue")
        self.fixno.place(x=485, y=140)
        self.fixne_ure = ttk.Combobox(self.frame, values=self.vrednosti, width=10)
        self.fixne_ure.place(x=558, y=140)
# ----------------------------------------------------------------------------------------------------------------------

        # dodajanje v listbox gumb
        self.add_button = Button(self.frame, text="Add", command=self.dodaj_delo)
        self.add_button.place(x=395, y=172)
        self.add_button.config(height=1, width=16)
# ----------------------------------------------------------------------------------------------------------------------

        # izberi mesec in letoza izračun
        self.Izracun_meseci = Label(self.frame, text="Calculate \nmonth-year", bg="steel blue")
        self.Izracun_meseci.place(x=315, y=202)

        self.mesec = ttk.Combobox(self.frame, values=self.meseci, width=10)
        self.mesec.place(x=395, y=209)
        self.leto = ttk.Combobox(self.frame, values=self.leta, width=10)
        self.leto.place(x=485, y=209)

        self.izrac_buton = Button(self.frame, text="Calculate", command=self.izracun)
        self.izrac_buton.place(x=595, y=208)

        # izpis plače
        self.Izracun_meseci = Label(self.frame, text="Pay: ", bg="steel blue")
        self.Izracun_meseci.place(x=315, y=250)
        self.placa = StringVar(self)  # <---------------
        self.update_label_placa = Label(self.frame,bg="steel blue", textvariable=self.placa, font= self.labelfont)
        self.update_label_placa.place(x=395, y=250)

# ----------------------------------------------------------------------------------------------------------------------

        # izpis napak
        self.napaka = StringVar(self)  # <---------------
        # self.napaka.set("sdth")

        self.update_label_napaka = Label(self.frame, textvariable=self.napaka, bg="steel blue", font=self.labelfont)
        self.update_label_napaka.place(x=315, y=300)

# ----------------------------------------------------------------------------------------------------------------------
        # gumb za izbrista vrstico iz listboxa
        self.delbtn = Button(self.frame, text="Delete", command=self.delete)
        self.delbtn.place(x=595, y=300)
# ----------------------------------------------------------------------------------------------------------------------
        #init za check box da postavi na mesto lahno b v check box configu naredu sam mi je blo tko hitreje
        self.doloci_checkbox()
#-----------------------------------------------------------------------------------------------------------------------

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
        self.listbox = Listbox(self.frame, height=21, width=32, selectmode=SINGLE, font="14")
        self.scroll = Scrollbar(self.frame, command=self.listbox.yview)

        self.listbox.configure(yscrollcommand=self.scroll.set, selectbackground="steel blue", bg="#DEDEDE", highlightthickness=0)
        self.listbox.pack(side=LEFT, fill=Y)
        self.scroll.pack(side=LEFT, fill=Y)

        data = open("Profile_data/" + self.glavno_ime + ".txt", "r")
        for x in data:
            if x == "\n":
                continue

            self.listbox.insert(0, x)

        data.close()

    def dodaj_delo(self):

        self.shra.create_new_folder_file(self.glavno_ime)
        
        # datoteka.write(name + "\n")
        datoteka = open("Profile_data/" + self.glavno_ime + ".txt", "a")

        if self.checkbox_izbira.get() == 1:
            datum = self.datum_window.get()
            day_ure = self.ure_dan.get()
            day_mony = self.denar_dan.get()
            night_ure = self.ure_noc.get()
            night_mony = self.denar_noc.get()

            if datum == "" or day_ure == "" or day_mony == "" or night_ure == "" or night_mony == "":
                self.napaka.set("Empty field!!!")
                print("prazno polje")
            else:
                datoteka.write(datum + " " + day_ure + "h " + day_mony + "€<><>" + night_ure + "h " + night_mony + "€\n")
                self.listbox.insert(0, datum + " " + day_ure + "h " + day_mony + "€<><>" + night_ure + "h " + night_mony + "€\n")
                print("napisano v file")
                self.napaka.set("Saved in file")
        else:
            datum = self.datum_window.get()
            ure = self.fixne_ure.get()
            denar_fix = self.fixne_denar.get()

            if datum == "" or ure == "" or denar_fix == "":
                self.napaka.set("Empty field!!!")
                print("prazno polje")
            else:
                datoteka.write(datum + " H= " + ure + " €= " + denar_fix + "\n")
                self.listbox.insert(0, datum + " H= " + ure + " €= " + denar_fix + "\n")
                print("napisano v file")
                self.napaka.set("Saved in file")

            print(datum+" "+ure+" "+denar_fix)
        datoteka.close()

    def izracun(self):
        podatki = open("Profile_data/" + self.glavno_ime + ".txt", "r")
        leto_ses = self.leto.get()
        mesec_ses = self.mesec.get()

        koncni_rezultat = 0

        if leto_ses == "" or mesec_ses == "":
            self.napaka("Apply month and year to calculate")
            print("Nisi izbral meseca in leta za izracun")
        else:

            datum_stevilka = self.meseci_dic.get(mesec_ses)
            for y in podatki:
                if y == "\n":
                    continue
                splitano_space = y.split(" ")
                datum_check = splitano_space[0][5:7]
                leto_check = splitano_space[0][0:4]

                if datum_check == datum_stevilka and leto_check == leto_ses:
                    dolzina = len(y)
                    print(dolzina)
                    if dolzina > 30:
                        day_h = float(splitano_space[1].replace("h",""))
                        day_mon = float(splitano_space[2].split("€<><>")[0])
                        night_h = float(splitano_space[2].split("€<><>")[1].replace("h", ""))
                        night_mon = float(splitano_space[3].replace("€",""))

                        koncni_rezultat += (day_mon*day_h)+(night_mon*night_h)
                    else:
                        sest_ure = float(splitano_space[2])
                        sest_denar = float(splitano_space[4])
                        koncni_rezultat += sest_ure*sest_denar


            self.placa.set(str(koncni_rezultat) + " €")

    def delete(self):
        # ta del je kritičen bi blo pametno da se napise kaksne stavke da ne zjebe vsega
        stevec = 0
        index_izbris = self.listbox.curselection() # vrne tuple wtf

        if index_izbris:
            self.listbox.delete(index_izbris[0])

            inverted_index = self.listbox.size() - index_izbris[0]
            print(inverted_index)
            with open("Profile_data/" + self.glavno_ime + ".txt", "r") as f:
                lines = f.readlines()
            with open("Profile_data/" + self.glavno_ime + ".txt", "w") as h:
                for line in lines:
                    if inverted_index == stevec:
                        stevec += 1
                        continue
                    h.write(line)
                    stevec += 1

    def dan_noc_ena_des(self):
        self.fixne_denar.configure(state="disabled")
        self.fixne_ure.configure(state="disabled")
        self.ure_dan.configure(state="normal")
        self.ure_noc.configure(state="normal")
        self.denar_dan.configure(state="normal")
        self.denar_noc.configure(state="normal")

        if self.checkbox_izbira_dva.get()==1:
            self.checkbox_izbira_dva.set(0)
            
    def fixno_ena_des(self):
        self.fixne_denar.configure(state="normal")
        self.fixne_ure.configure(state="normal")
        self.ure_dan.configure(state="disabled")
        self.ure_noc.configure(state="disabled")
        self.denar_dan.configure(state="disabled")
        self.denar_noc.configure(state="disabled")

        if self.checkbox_izbira.get()==1:
            self.checkbox_izbira.set(0)

    def doloci_checkbox(self):
        self.checkbox_izbira_dva.set(1)
        self.fixne_denar.configure(state="normal")
        self.fixne_ure.configure(state="normal")
        self.ure_dan.configure(state="disabled")
        self.ure_noc.configure(state="disabled")
        self.denar_dan.configure(state="disabled")
        self.denar_noc.configure(state="disabled")


if __name__ == '__main__':
    root = Tk()
    prvo_okno = LoginFrame(root)
    root.mainloop()
