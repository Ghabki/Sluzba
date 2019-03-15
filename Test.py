from tkinter import *

master = Tk()

frame = Frame(master)
frame.pack(fill = BOTH)
master.geometry("600x300")

scrollbar = Scrollbar(frame)
scrollbar.pack(side = RIGHT,fill = Y)

listbox = Listbox(frame)
listbox.pack(fill = BOTH)

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

for i in range(0,100):
    listbox.insert(END,'Item {}'.format(i + 1))

master.mainloop()