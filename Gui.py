from tkinter import *
from tkinter import ttk
from Sluzba.shranjevanje import *
from Sluzba.main_screen_code import *
#todo zrihtaj da napise opozorila za uporabo asci znakov bla bla blank line fix


class LoginFrame(Frame):
    shra = Shranjevanje()
    shra.register_file()

    def __init__(self, master):
        super().__init__(master)
        # to sem js dodau
        self.master.title("My work h app")
        self.master.geometry("300x100")
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

            if self.shra.get_x() == 1:
                self.besedilo.set("ze obstaja tak username")
                break
            else:
                self.besedilo.set("Registriran")
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

        self.master.deiconify()

        self.master.title("My work h app")
        self.master.geometry("600x300")
        self.master.iconbitmap(r"favicon.ico")
        self.master.configure(background='#22272d')
        # overrida kar naredi X button pri oknu
        self.master.protocol("WM_DELETE_WINDOW", self.exit_fix)

        self.frame = Frame(self)

        self.treeView = ttk.Treeview(self)

        self.quitButton = Button(self, text='Quit', width=25, command=self.close_window)
        self.quitButton.pack()
        self.treeView.pack()
        self.pack()

    # def close_windows(self):
    # root.destroy()
    @staticmethod
    def exit_fix():
        print("destroyed")
        root.destroy()

    def close_window(self):
        pass


if __name__ == '__main__':
    root = Tk()
    prvo_okno = LoginFrame(root)
    root.mainloop()
