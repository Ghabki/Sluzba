import datetime





class Listbox_Shranjevanje:









#string datum
    def datum(self):
        now = str(datetime.datetime.now().date())
        print(now)
        return now




razred = Listbox_Shranjevanje()
razred.datum()