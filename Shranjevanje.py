import os
import uuid
import hashlib


class Shranjevanje:

    def __init__(self):
        print("Ghabki the creator")
        self.x = 0
        self.rak = True

    def get_x(self):
        return self.x

    def set_x(self, y):
        self.x = y

    def set_ali_pravilen_ascii(self, omg):
        self. rak = omg

    def get_ali_pravilen_ascii(self):
        return self.rak

    def hash_password(self, password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def register_file(self):
        if os.path.isfile('registracija.txt'):
            print("file obstaja")
        else:
            open("registracija.txt", "w+")
            print("file ni obstajal in je bil narejen vi mapi kjer je program")

    def search(self, username):
        file = open("registracija.txt", "r")
        if os.stat("registracija.txt").st_size == 0:
            file.close()
            print("kj je to")
            return False

        for line in file:
            new_line = line.rstrip()
            pravilen_line = new_line.split(",")

            if pravilen_line[0] == username:  # da vsebuje ze noter
                self.set_x(1)
                print("koj k")
                file.close()
                return True
            else:  # ne vseebuje noter
                continue

        self.set_x(0)
        file.close()
        return False

    def registracija(self, username, password):
        zapis = open("registracija.txt", "a")
        preveri = self.search(username)
        asci_preverjanje = self.poglej_za_asci(username)

        if asci_preverjanje:
            if preveri:
                print("ze vsebuje ta username")
                zapis.close()

            elif not preveri:
                print("registriran")
                passwrd = self.hash_password(password)
                zapis.write(username + "," + passwrd + "\n")
                zapis.close()
                self.set_ali_pravilen_ascii(True)  # ce je pravilen stavek se izvede to
                print("asci true")
        else:
            self.set_ali_pravilen_ascii(False)  # ce je nepravilen se izvede to
            print("ascii false")
            zapis.close()

    def prijava(self, username, password):
        print("logging in")

        if self.search(username) == True:
            file = open("registracija.txt", "r")

            if os.stat("registracija.txt").st_size == 0:
                file.close()
                return False

            for line in file:
                new_line = line.rstrip()
                pravilen_line = new_line.split(",")
                if pravilen_line[0] == username:
                    if self.check_password(pravilen_line[1], password) == True:
                        file.close()
                        return True
                    else:
                        file.close()
                        return False

        print("agsfd")

    def poglej_za_asci(self, besedilo):
        # ni fast, itak koga zanima
        return all(ord(c) < 128 for c in besedilo)

# s = Shranjevanje()
