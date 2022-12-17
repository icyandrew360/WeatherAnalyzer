#Code by Andrew Howe and John Manoli

import numpy

from FileIO import FileIO

from Date import Date

f = FileIO()

d = Date()

class TemperatureData:
    def __init__(self):

        self.minTemperature = []
        self.maxTemperature = []
        self.snowFall = []
        for i in range (len(f.dataTable)):
            self.minTemperature.append(f.dataTable[i,3])
        for i in range (len(f.dataTable)):
            self.maxTemperature.append(f.dataTable[i,2])
        for i in range (len(f.dataTable)):
            self.snowFall.append(f.dataTable[i,4])


def main():
    t = TemperatureData()


if __name__ == "__main__":
    main()

    

