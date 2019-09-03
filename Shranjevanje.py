import os
import uuid
import hashlib 
vraca_name = None

class Shranjevanje:

    def __init__(self):
        print("Ghabki the creator")
        self.x = 0
        self.rak = True
        self.space = 0

        #to global nebi rablo, lahko bi samo klicau spremenljivko z objektom
        global vraca_name

    def set_space(self, a):
        self.space = a

    def get_space(self):
        return self.space

    def get_x(self):
        return self.x

    def set_x(self, y):
        self.x = y

    def set_ali_pravilen_ascii(self, set_true_or_false):
        self.ascii_check = set_true_or_false

    def get_ali_pravilen_ascii(self):
        return self.ascii_check

    def hash_password(self, password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def register_file(self):
        try:

            if os.path.isdir("Reg_data"):
                print("directory ok")
            else:
                os.mkdir("Reg_data")
                print("Folder narejen")

            if os.path.isfile("Reg_data/Reg_data.txt"):
                print("file obstaja")
            else:
                open("Reg_data/Reg_data.txt", "w+")
                print("file ni obstajal in je bil narejen vi mapi kjer je program")
        except:
            print("Neki se zalomlo pri kreiranju map")

    def search(self, username):
        
        try:
            file = open("Reg_data/Reg_data.txt", "r")
        except:
            file.close()
            print("Za odpret file se je zalomlo")

        try:    
            if os.stat("Reg_data/Reg_data.txt").st_size == 0:
                file.close()
                print("kj je to")
                return False

            for line in file:
                new_line = line.rstrip()
                pravilen_line = new_line.split(",")

                if pravilen_line[0] == username:  # da vsebuje ze noter
                    self.set_x(1)
                    print("iskanje vredu")
                    file.close()
                    return True
                else:  # ne vseebuje noter
                    continue
        except:
            print("neki se zalomlo pri branju file")
            file.close()           

        self.set_x(0)
        file.close()
        return False

    def registracija(self, username, password):

        try:
            zapis = open("Reg_data/Reg_data.txt", "a")
        except:
            print("Napaka z datoteko pri registraciji")
        preveri = self.search(username)

        asci_preverjanje = self.poglej_za_asci(username)
        space_preverjanje = self.poglej_za_space(username)

        if space_preverjanje:
            zapis.close()
        else:
            self.set_space(0)
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
            try:
                file = open("Reg_data/Reg_data.txt", "r")
            except:
                print("Napaka z datoteko pri prijavi")
                file.close()
            if os.stat("Reg_data/Reg_data.txt").st_size == 0:
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

        print("ni pravi username ali password")

    def poglej_za_asci(self, besedilo):
        # ni fast, itak koga zanima
        return all(ord(c) < 128 for c in besedilo)

    def poglej_za_space(self, ime):
        if " " in ime or not ime:
            print("no spaces or blank line")
            self.set_space(1)
            return True
        else:
            self.set_space(0)
            print("OK--ne vsebuje presledkov")
            return False

    def create_new_folder_file(self, ime_datoteke):
        try:
            if os.path.isdir("Profile_data"):
                print("profile data folder ok")
            else:
                os.makedirs("Profile_data")
                print("Profile data folder narejen")

            if os.path.isfile("Profile_data/"+ime_datoteke+".txt"):
                print("profile FILE  ok")
            else:
                open("Profile_data/"+ime_datoteke+".txt", "a")
                print("Profile data folder narejen")
        except:
            print("napaka pri kreiranju datotek")
#nebi bilo potrebno>
def get_username(self):
    return self.vraca_name


def set_username(self, name):
    self.vraca_name = name
