from tkinter import *
from Sluzba.shranjevanje import Shranjevanje, pregledano


#todo zrihtaj da napise opozorila za uporabo asci znakov



class LoginFrame(Frame):
    shra = Shranjevanje()
    shra.register_file()

    def __init__(self, master):
        super().__init__(master)

        self.master.title("My work h app")
        self.master.geometry("300x100")
        self.master.iconbitmap(r"favicon.ico")

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.besedilo= StringVar(self)
        self.update_label=Label(self, textvariable=self.besedilo)

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        self.update_label.grid(row= 3, sticky=E)






        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=2 , column= 1)

        self.regbtn = Button(self, text="Register", command=self._register_btn_clicked)
        self.regbtn.grid(row=3 , column= 1)

        self.pack()


    def _register_btn_clicked(self):

        while True:
            username = self.entry_username.get()
            password = self.entry_password.get()

            self.shra.registracija(username, password)

            if pregledano == 1:
                print("1")
                self.besedilo.set("ze obstaja tak username")
                break
            else:
                self.besedilo.set("Registriran")
                break



    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()




        # print(username, password)






root = Tk()




prvo_okno = LoginFrame(root)

root.mainloop()