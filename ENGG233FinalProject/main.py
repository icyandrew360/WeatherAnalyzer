#Code by Andrew Howe and John Manoli

import numpy as np

from FileIO import FileIO

from TemperatureData import TemperatureData

from Date import Date

from Chart import Chart

from WeatherAnalyzer import WeatherAnalyzer

import matplotlib.pyplot as pyplot

f = FileIO()

t = TemperatureData()

d = Date()

w = WeatherAnalyzer()

def main():
    print('')
    print ("1- Get Minimum Temperature of 1990-2019 \n2- Get Maximum Temperature of 1990-2019 \n3- Get Minimum Temperature of 1990-2019 Annually")
    print ("4- Get Maximum Temperature of 1990-2019 Annually \n5- Get Average Snowfall between 1990-2019 Annually")
    print('')
    option = int(input("Please enter the number of the option you would like to see: "))
    print('')

    if option == 1:
        minTempData = w.getMinTemp()
        print (f"The lowest recorded temperature from the data was {minTempData[0]} degrees, in year {minTempData[1]}, month {minTempData[2]}")
        print('')

    elif option == 2:
        maxTempData = w.getMaxTemp()
        print (f"The highest recorded temperature from the data was {maxTempData[0]} degrees, in year {maxTempData[1]}, month {maxTempData[2]}")
        print('')

    elif option == 3:
        annualMinTempData = w.getMinTempAnnually()
        for i in range (30):
            print (f"In {annualMinTempData[i,0]}, the lowest recorded temp was {annualMinTempData[i,1]} degrees.")
        print('')

    elif option == 4:
        annualMaxTempData = w.getMaxTempAnnually()
        for i in range (30):
            print (f"In {annualMaxTempData[i,0]}, the highest recorded temp was {annualMaxTempData[i,1]} degrees.")
        print('')

    elif option == 5:
        annualSnowFallData = w.getAvgSnowFallAnnually()
        for i in range (30):
            print (f'In {annualSnowFallData[i,0]}, the average recorded snowfall was {annualSnowFallData[i,1]} cm.')
        print('')
        
    else:
        print("Invalid Choice Inputted")
        print('')

if __name__ == "__main__":
    main()