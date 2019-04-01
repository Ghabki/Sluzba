from tkinter import *
from Sluzba.shranjevanje import *
from Sluzba.date_picker import *
#from Sluzba.main import *



class LoginFrame(Frame):
    shra = Shranjevanje()
    shra.register_file()


    def __init__(self, master):
        super().__init__(master)

        self.master.resizable(False, False)
        # to sem js dodau
        self.master.title("My work h app")
        self.master.geometry("300x105")
        self.master.iconbitmap(r"favicon.ico")

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")
        # string var za spreminjajoc se label
        self.besedilo = StringVar(self)
        self.update_label = Label(self, textvariable=self.besedilo)

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        self.update_label.grid(row=3, sticky=E)
        # da fokusira okence
        self.entry_username.focus()

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=2, column=1)

        self.regbtn = Button(self, text="Register", command=self._register_btn_clicked)
        self.regbtn.grid(row=3, column=1)

        self.pack()

    def _register_btn_clicked(self):

        while True:
            username = self.entry_username.get()
            password = self.entry_password.get()

            self.shra.registracija(username, password)

            asciii = self.shra.get_ali_pravilen_ascii()

            if asciii:
                rak = self.shra.get_x()
                if rak == 1:
                    self.besedilo.set("ze obstaja tak username")
                    break
                elif rak == 0:
                    self.besedilo.set("Registriran")
                    break
                break
            else:
                self.besedilo.set("Uporavi samo ascii \n znake")
                break

    def _login_btn_clicked(self):
        # print("Clicked")

        while True:
            username = self.entry_username.get()
            password = self.entry_password.get()

            if self.shra.prijava(username, password):
                # NEVEM KAKO TO DELA NEVEM ZAKAJ TO DELA NEVEM ZAKAJ JE TO TAKO RAKAVO!!
                self.master.withdraw()
                self.glavno_okno = Toplevel(self.master)
                MainScreen(self.glavno_okno)
                break
            else:
                self.besedilo.set("Napačni username \n ali geslo")
                break


class MainScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        #self.master.resizable(False, False)
        self.master.title("My work h app")
        self.master.geometry("650x345")
        self.master.iconbitmap(r"favicon.ico")
        self.master.configure(background='gray14')
        # overrida kar naredi X button pri oknu
        self.master.protocol("WM_DELETE_WINDOW", self.exit_fix)

        self.frame = Frame(self.master, width=345, background="steel blue")
        #self.frame.grid(row=0, column=0)
        self.frame.pack(fill=X)

        #self.top_frame = Frame(self.master, width=389, height=345, pady=3, background="gray14")
        #self.top_frame.grid(row=0, column=1)
        # naredi listbox
        self.create_list_box()

        self.entry_username = Entry(self.frame)
        self.entry_username.place(x=300, y=0)
        self.entry_username.pack()


        #self.datum = Label(self.frame, text=__doc__)
        #self.datum.place(x=500, y=150)
        self.regbtn = Button(self.frame, text="Register", command=self.lolek)
        self.regbtn.place(x=300, y=50)

        self.entry_usernameee = Entry(self.frame)
        self.entry_usernameee.place(x=400, y=200)


        self.nice = Datepicker(self.frame)
        self.nice.place(x=300, y=90)





        #self.logbtnn = Button(self.top_frame, text="Login", command=self.lolek)
        #self.logbtnn.grid(row=0, column=1)

    def lolek(self):
        #a = self.Datepicker.get()
        print("fdshgsghdf")
        print(self.nice.current_text)



    def create_list_box(self):
        listbox = Listbox(self.frame, height=21, width=40, selectmode=SINGLE)
        scroll = Scrollbar(self.frame, command=listbox.yview)

        listbox.configure(yscrollcommand=scroll.set)
        listbox.pack(side=LEFT, fill=Y)
        scroll.pack(side=LEFT, fill=Y)

        for item in range(30):
            listbox.insert(END, item)

    @staticmethod
    def exit_fix():
        print("destroyed")
        root.destroy()


if __name__ == '__main__':
    root = Tk()
    prvo_okno = LoginFrame(root)
    root.mainloop()
