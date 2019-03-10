import datetime

class PridobitevPodatkov:
    vnos = 0

    def vprasaj(self):

        while True:
            try:
                vnos = int(input("Vnesi število ur"))
                print(vnos)
                break
            except ValueError:
                print('vnesi stevilko z "," ')
        return vnos









#string datum
    def datum(self):
        now = str(datetime.datetime.now().date())
        print(now)
        return now




razred = PridobitevPodatkov()
razred.datum()