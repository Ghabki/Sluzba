from tkinter import *
from Sluzba.shranjevanje import *


#todo zrihtaj da napise opozorila za uporabo asci znakov

class LoginFrame(Frame):
    shra = Shranjevanje()
    shra.register_file()

    def __init__(self, master):
        super().__init__(master)
        #to sem js dodau
        self.master.title("My work h app")
        self.master.geometry("300x100")
        self.master.iconbitmap(r"favicon.ico")

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")
        #string var za spreminjajoc se label
        self.besedilo= StringVar(self)
        self.update_label=Label(self, textvariable=self.besedilo)

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        self.update_label.grid(row=3, sticky=E)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=2, column=1)

        self.regbtn = Button(self, text="Register", command=self._register_btn_clicked)
        self.regbtn.grid(row=3, column=1)

        self.pack()

    def change(self, frame):
        self.frame.pack_forget()  # delete currrent frame
        self.frame = frame(self)
        self.frame.pack()


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
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.openFrame()


    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        subFrame = MainScreen()
        handler = lambda: self.onCloseOtherFrame(subFrame)
        btn = Tk.Button(subFrame, text="Close", command=handler)
        btn.pack()

    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()






        #self.newWindow = Toplevel(self.master)
        #self.app = MainScreen(self.newWindow)





        # print(username, password)
class MainScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()




class GUI(Tk):
    def __init__(self, *args):
        Tk.__init__(self, *args)



        # Creation of all the relevant Frames

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(200, weight=1)
        container.grid_columnconfigure(200, weight=1)

        self.frames = {}

        for F in (LoginFrame, MainScreen):
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.raise_frame(LoginFrame)

        # Frame manipulation functions

    def raise_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def update_frame(self, page_name):
        frame = self.frames[page_name]
        frame.update()

    def destroy_frame(self, page_name):
        frame = self.frames[page_name]
        frame.destroy()


#if __name__ == "__main__":
 #   app = Mainframe()
  #  app.mainloop()

#if __name__ == "__main__":
 #   gui = GUI()
  #  gui.mainloop()





if __name__ == '__main__':
    root = Tk()
    prvo_okno = LoginFrame(root)
    root.mainloop()