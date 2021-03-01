import csv

from tkinter import *

def loadArchive(archive):
    return open(archive, newline='')

def getData(archive):
    reader = csv.DictReader(archive, delimiter=',')
    return reader


archiveCsv = loadArchive(r'C:\Users\andre\PycharmProjects\PythonCars\CarRentalData.csv')
data = getData(archiveCsv)

rentedTesla = 0
rentedToyota = 0
rentedFord = 0
rentedMercedes = 0
rentedChevrolet = 0
rentedJeep = 0
rentedPorsche = 0
rentedVolkswagen = 0

for car in data:
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


class Application:

    def __init__(self, master="none") -> None:
        self.defaultFont = ("Arial", 10)

        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["pady"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["pady"] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 20
        self.fourthContainer.pack()

        self.fifthContainer = Frame(master)
        self.fifthContainer["pady"] = 20
        self.fifthContainer.pack()

        self.sixthContainer = Frame(master)
        self.sixthContainer["pady"] = 20
        self.sixthContainer.pack()

        self.seventhContainer = Frame(master)
        self.seventhContainer["pady"] = 20
        self.seventhContainer.pack()

        self.eighthContainer = Frame(master)
        self.eighthContainer["pady"] = 20
        self.eighthContainer.pack()

        self.messagea = Label(self.firstContainer, text="", font=self.defaultFont)
        self.messagea.pack()

        self.messageb = Label(self.secondContainer, text="", font=self.defaultFont)
        self.messageb.pack()

        self.messagec = Label(self.thirdContainer, text="", font=self.defaultFont)
        self.messagec.pack()

        self.messaged = Label(self.fourthContainer, text="", font=self.defaultFont)
        self.messaged.pack()

        self.messagee = Label(self.fifthContainer, text="", font=self.defaultFont)
        self.messagee.pack()

        self.messagef = Label(self.sixthContainer, text="", font=self.defaultFont)
        self.messagef.pack()

        self.messageg = Label(self.seventhContainer, text="", font=self.defaultFont)
        self.messageg.pack()

        self.messageh = Label(self.eighthContainer, text="", font=self.defaultFont)
        self.messageh.pack()

        self.messagea["text"] = "Rented cars by Tesla: " + str(rentedTesla)
        self.messageb["text"] = "Rented cars by Toyota: " + str(rentedToyota)
        self.messagec["text"] = "Rented cars by Ford: " + str(rentedFord)
        self.messaged["text"] = "Rented cars by Mercedes: " + str(rentedMercedes)
        self.messagee["text"] = "Rented cars by Chevrolet: " + str(rentedChevrolet)
        self.messagef["text"] = "Rented cars by Jeep: " + str(rentedJeep)
        self.messageg["text"] = "Rented cars by Porsche: " + str(rentedPorsche)
        self.messageh["text"] = "Rented cars by Volkswagen: " + str(rentedVolkswagen)

root = Tk()
Application(root)
root.mainloop()

