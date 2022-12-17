#Code by Andrew Howe and John Manoli

import numpy

from FileIO import FileIO

from TemperatureData import TemperatureData

from Date import Date

import matplotlib.pyplot as pyplot

f = FileIO()

t = TemperatureData()

d = Date()

class Chart:
    def __init__(self, title, xlabel, ylabel, x, y):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.x = x
        self.y = y

    def drawLineChart(self):
    
        pyplot.title(self.title)
        pyplot.ylabel(self.ylabel)
        pyplot.xlabel(self.xlabel)

        pyplot.plot(self.x, self.y, marker='o')  
        pyplot.show()

    def drawBarChart(self):
        
        pyplot.bar(self.x, self.y, color='blue')
        pyplot.title(self.title)
        pyplot.xlabel(self.xlabel)
        pyplot.ylabel(self.ylabel)

        pyplot.show()
        


# def main():

#     x = []

#     y = []

#     c = Chart(x, y)
#     #c.drawLineChart()

# if __name__ == "__main__":
#     main()