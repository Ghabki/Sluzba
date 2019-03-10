import tkinter

from Sluzba.shranjevanje import *

########################################################################
class OtherFrame(Toplevel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("otherFrame")


########################################################################
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------

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

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=2, column=1)

        self.regbtn = Button(self, text="Register", command=self._register_btn_clicked)
        self.regbtn.grid(row=3, column=1)

        self.pack()

    btn = Button(self.frame, text="Open Frame", command=self.openFrame)
    btn.pack()

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        subFrame = OtherFrame()
        handler = lambda: self.onCloseOtherFrame(subFrame)
        btn = Button(subFrame, text="Close", command=handler)
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


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()