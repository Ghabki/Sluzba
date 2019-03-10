import os

class Shranjevanje:


    def register_file(self):
        if os.path.isfile('registracija.txt'):
            print("obstaja")
        else:
            open("registracija.txt", "w+")

            print("dfak")


    def search(self, username):
        file = open("registracija.txt", "r")


        for line in file:
            new_line = line.rstrip()
            pravilen_line = new_line.split(",")
            for i in pravilen_line:
                if i[0] == username:
                    file.close()
                    return True
                else:
                    file.close()
                    return False



#print(pravilen_line)

    def registracija(self):
























    def create_file(self):
        vnos = str(input("Vnesi ime"))
        f = open(vnos+".txt", "w+")


s= Shranjevanje()
s.search()
