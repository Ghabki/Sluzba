from tkinter import *
import Shranjevanje
#todo zrihtaj da napise opozorila za uporabo asci znakov




class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)


        self.master.title("My work h app")
        self.master.geometry("300x100")
        self.master.iconbitmap(r"favicon.ico")

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)


        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.regbtn = Button(self, text="Login", command=self._register_btn_clicked)
        self.regbtn.grid(columnspan=3)

        self.pack()


    def _register_btn_clicked(self):
        print("dasf")



    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()
        poisci = Shranjevanje()
        poisci.search(username)

        # print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")




root = Tk()




prvo_okno = LoginFrame(root)

root.mainloop()