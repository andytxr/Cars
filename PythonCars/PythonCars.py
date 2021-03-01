import csv
from tkinter import *

class Application:

    def __init__(self, master=None):

        self.defaultFont = ("Arial", "10")

        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()

        self.title = Label(self.firstContainer, text="Car Rental Data Identifier")
        self.title["font"] = ("Arial", 10, "bold")
        self.title.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["pady"] = 10
        self.secondContainer.pack()
        self.thirdContainer = Frame(master)
        self.thirdContainer["pady"] = 10
        self.thirdContainer.pack()

        self.desc = Label(self.secondContainer, text="Enter the brand to return the number of vehicles rented by it.")
        self.desc["font"] = ("Arial", 8, "italic")
        self.desc.pack()
        self.brands = Label(self.thirdContainer, text="Brands available: Chevrolet, Ford, Jeep, Mercedes, Porsche, Tesla, Toyota and Volkswagen")
        self.brands["font"] = ("Calibri", 8)
        self.brands.pack()

        self.brandContainer = Frame(master)
        self.brandContainer["padx"] = 20
        self.brandContainer.pack()

        self.brandLabel = Label(self.brandContainer, text="Brand name", font=self.defaultFont)
        self.brandLabel.pack(side=LEFT)

        self.brandName = Entry(self.brandContainer)
        self.brandName["width"] = 30
        self.brandName["font"] = self.defaultFont
        self.brandName.pack(side=LEFT)

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 20
        self.fourthContainer.pack()

        self.firstWidget = Frame(master)
        self.firstWidget.pack()

        self.verify = Button(self.firstWidget, font=self.defaultFont, text="Done", bg="purple", command=self.brandShow)
        self.verify.pack()

        self.msg = Label(self.fourthContainer, text=" ", font=self.defaultFont)
        self.msg.pack()

    def brandShow(self):

        def loadArchive(archive):
            return open(archive, newline="")

        def getData(archive):
            reader = csv.DictReader(archive, delimiter=",")
            return reader

        archiveCsv = loadArchive(r'C:\Users\yourFolder\yourFolder\PythonCars\CarRentalData.csv')
        data = getData(archiveCsv)

        rentedChevrolet = 0
        rentedFord = 0
        rentedMercedes = 0
        rentedPorsche = 0
        rentedTesla = 0
        rentedToyota = 0
        rentedVolkswagen = 0
        rentedJeep = 0

        for car in data:
            brand = self.brandName.get().lower()
            car = dict(car)
            if (car["vehicle.make"] == "Tesla"):
                rentedTesla = rentedTesla + 1
            elif (car["vehicle.make"] == "Toyota"):
                rentedToyota = rentedToyota + 1
            elif (car["vehicle.make"] == "Ford"):
                rentedFord = rentedFord + 1
            elif (car["vehicle.make"] == "Mercedes-Benz"):
                rentedMercedes = rentedMercedes + 1
            elif (car["vehicle.make"] == "Chevrolet"):
                rentedChevrolet = rentedChevrolet + 1
            elif (car["vehicle.make"] == "Jeep"):
                rentedJeep = rentedJeep + 1
            elif (car["vehicle.make"] == "Porsche"):
                rentedPorsche = rentedPorsche + 1
            elif (car["vehicle.make"] == "Volkswagen"):
                rentedVolkswagen = rentedVolkswagen + 1

            if (brand == "chevrolet"):
                self.msg["text"] = "Rented cars by Chevrolet: " + str(rentedChevrolet)
            elif (brand == "ford"):
                self.msg["text"] = "Rented cars by Ford: " + str(rentedFord)
            elif (brand == "jeep"):
                self.msg["text"] = "Rented cars by Jeep: " + str(rentedJeep)
            elif (brand == "mercedes"):
                self.msg["text"] = f"Rented cars by Mercedes: " + str(rentedMercedes)
            elif (brand == "porsche"):
                self.msg["text"] = "Rented cars by Porsche: " + str(rentedPorsche)
            elif (brand == "tesla"):
                self.msg["text"] = "Rented cars by Tesla: " + str(rentedTesla)
            elif (brand == "toyota"):
                self.msg["text"] = "Rented cars by Toyota: " + str(rentedToyota)
            elif (brand == "volkswagen"):
                self.msg["text"] = "Rented cars by Mercedes: " + str(rentedMercedes)
            else:
                self.msg["text"] = "The mark is misspelled or does not exist in the database."
root = Tk()
Application(root)
root.mainloop()





