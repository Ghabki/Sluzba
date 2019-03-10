import os
import uuid
import hashlib


class Shranjevanje:

    def __init__(self):
        self.x = 0

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def hash_password(self,password):
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
        self.x = 1
        file = open("registracija.txt", "r")
        if os.stat("registracija.txt").st_size == 0:
            file.close()
            return False

        for line in file:
            new_line = line.rstrip()
            pravilen_line = new_line.split(",")

            if pravilen_line[0] == username:  # da vsebuje ze noter
                file.close()
                self.set_x(1)
                return True
            else:  #ne vseebuje noter
                continue

        file.close()
        self.set_x(0)
        return False

    def registracija(self, username, password):
        zapis = open("registracija.txt", "a")
        if self.search(username):
            print("ze vsebuje ta username")
            zapis.close()
        else:
            passwrd = self.hash_password(password)
            zapis.write(username + "," + passwrd + "\n")
            zapis.close()

    def prijava(self, username, password):







        print("agsfd")



s = Shranjevanje()


