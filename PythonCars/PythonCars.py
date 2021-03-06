import csv
import webbrowser
import asyncio
from tkinter import *

loop = asyncio.get_event_loop()
new = 2
class Application:

    def __init__(self, master=None):

        self.defaultFont = ("Arial", "10")

        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer["background"] = "pink"
        self.firstContainer.pack()

        self.title = Label(self.firstContainer, text="🚗 Car Rental Data Identifier 🚗", bg="pink")
        self.title["font"] = ("Arial", 10, "bold")
        self.title.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["pady"] = 10
        self.secondContainer["background"] = "pink"
        self.secondContainer.pack()
        self.thirdContainer = Frame(master)
        self.thirdContainer["pady"] = 10
        self.thirdContainer["background"] = "pink"
        self.thirdContainer.pack()

        self.desc = Label(self.secondContainer, text="Enter the brand to return the number of vehicles rented by it.", bg="pink")
        self.desc["font"] = ("Arial", 8, "italic")
        self.desc.pack()

        self.brandsButton = Button(self.thirdContainer, text="Brands available", font=self.defaultFont, bg="purple", command=self.brandsAvailable)
        self.brandsButton.pack()

        self.brandContainer = Frame(master)
        self.brandContainer["padx"] = 20
        self.brandContainer["background"] = "pink"
        self.brandContainer.pack()

        self.brandLabel = Label(self.brandContainer, text="Brand name:", font=self.defaultFont, bg="pink")
        self.brandLabel.pack(side=LEFT)

        self.brandName = Entry(self.brandContainer)
        self.brandName["width"] = 30
        self.brandName["font"] = self.defaultFont
        self.brandName.pack(side=LEFT)

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 20
        self.fourthContainer["background"] = "pink"
        self.fourthContainer.pack()

        self.firstWidget = Frame(master)
        self.firstWidget["background"] = "pink"
        self.firstWidget.pack()

        self.verify = Button(self.firstWidget, font=self.defaultFont, text="Done", bg="green", command=self.brandShow)
        self.verify.pack(side=LEFT)

        self.msg = Label(self.fourthContainer, text=" ", font=self.defaultFont, bg="pink")
        self.msg.pack()

        self.quit = Button(self.firstWidget, font=self.defaultFont, text="Quit", bg="red", command=root.quit)
        self.quit.pack(side=RIGHT)

    def brandsAvailable(self):
        url=r"BrandsAvailable.html"
        webbrowser.open(url, new=new)

    def brandShow(self):


        async def loadArchive(archive):
            return  open(archive, newline="")

        archiveCsv = loop.run_until_complete(loadArchive(r'CarRentalData.csv'))

        async def getData(archive):
            reader = csv.DictReader(archive, delimiter=",")
            return reader

        data = loop.run_until_complete(getData(archiveCsv))

        rented_cars = {}

        for car in data:
            brand = self.brandName.get()
            car = dict(car)

            if not car["vehicle.make"].lower() in rented_cars:
                rented_cars[car["vehicle.make"].lower()] = 0

            rented_cars[car["vehicle.make"].lower()] += 1

        if brand in rented_cars:
            self.msg["background"] = "pink"
            self.msg["text"] = "Rented cars by " + brand.capitalize() + ": " + str(rented_cars[brand])
        else:
            self.msg["background"] = "pink"
            self.msg["text"] = "The brand is misspelled or does not exist in the database."
root=Tk()
Application(root)
root.title("Car Rental Data")
root.configure(background="pink")
root.mainloop()

