import os
import uuid
import hashlib



class Shranjevanje:


    def hash_password(password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()





    def register_file(self):
        if os.path.isfile('registracija.txt'):
            print("obstaja")
        else:
            open("registracija.txt", "w+")

            print("dfak")


    def search(self, username):
        file = open("registracija.txt", "r")
        if os.stat("registracija.txt").st_size == 0:
            file.close()
            return False


        for line in file:

            new_line = line.rstrip()
            pravilen_line = new_line.split(",")


            if pravilen_line[0] == username:  # da vsebuje ze noter
                file.close()
                return True
            else:  #ne vseebuje noter
                continue
            file.close()



    def registracija(self, username, password):
        zapis = open("registracija.txt", "a")
        if self.search(username):
            print("ze vsebuje ta username")
            zapis.close()
        else:
            zapis.write(username + "," + password + "\n")
            zapis.close()

























    def create_file(self):
        vnos = str(input("Vnesi ime"))
        f = open(vnos+".txt", "w+")


s= Shranjevanje()
s.registracija("bubu", "polek")
