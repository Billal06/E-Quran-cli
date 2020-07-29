# Code by Billal Fauzan
# Project name E-Quran
# Thanks To https://github.com/rioastamal/quran-json

import json
import getpass
import os

class Quran:
    def __init__(self):
        self.data = []
    
    def banner(self):
        print ("     =} Welcome to E-Quran {=")
        print ("          {Code by Billal} ")
 
    def openSurah(self, index):
        o = open("surah/" + str(index) + ".json")
        j = json.loads(o.read())
        return j
    
    def getSurah(self):
        for a in range(1, 115):
            self.data.append(self.openSurah(a))
            
    def showSurah(self, pilihan):
        os.system("cls" if os.name == "nt" else "clear")
        arab = self.data[pilihan][str(pilihan + 1)]["text"]
        id = self.data[pilihan][str(pilihan + 1)]["translations"]["id"]["text"]
        for ayat in range(len(arab)):
            print (str(ayat + 1) + "). " + arab[str(ayat + 1)])
            print ("   " + id[str(ayat + 1)])
            getpass.getpass("Enter to continue..")
            
    def choiceSurah(self):
        pilihan = None
        for a in range(len(self.data)):
            print (str(a + 1) + "). " + self.data[a][str(a + 1)]["name_latin"])
            
        
        while True:
            try:
                i = input("Pilih ~> ")
                if i.isdigit() == True:
                    if int(i) > len(self.data):
                        print ("[!] Pilihan kamu tidak ditemukan")
                    else:
                        pilihan = int(i) - 1
                        break
                else:
                    print ("[!] Masukan angka!")
            except IndexError:
                print ("[!] Pilihan kamu tidak ditemukan")
            
        self.showSurah(pilihan)
    def main(self):
        self.getSurah()
        self.choiceSurah()
        
if __name__ == "__main__":
    quran = Quran()
    quran.main()