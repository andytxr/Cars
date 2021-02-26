import csv

from tkinter import *
from tkinter.messagebox import *

def loadArchive (archive):
    return open(archive, newline='')

def getData(archive):
    reader = csv.DictReader(archive, delimiter=',')
    return reader

archiveCsv=loadArchive(r'C:\Users\youruser\yourfolder\PythonCars\CarRentalData.csv')
data=getData(archiveCsv)

rentedTesla=0

for car in data:
    car=dict(car)
    if(car["vehicle.make"]=="Tesla"):
        rentedTesla= rentedTesla+1

class Application: 
    def __init__(self, master="none") -> None:

        self.defaultFont=("Arial",10)
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.message = Label(self.firstContainer, text="", font=self.defaultFont)
        self.message.pack()
            
        self.message["text"]="Rented cars by Tesla: " + str(rentedTesla)

        
root = Tk()
Application(root)
root.mainloop()

