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
    print ("6- Get Average Temperature of 1990-2019 Annually \n7- Show Linechart of Minimum Temperatures of 1990-2019 Annually")
    print ("8- Show Linechart of Minimum Temperatures of 1990-2019 Annually \n9- Show Barchart of Average Snowfall between 1990-2019 Annually")
    print ("10- Show Barchart of Average Temperatures of 1990-2019 Annually")
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
    
    elif option == 6:
        annualAvgTempData = w.getAvgTempAnnually()
        for i in range (30):
            print (f'In {annualAvgTempData[i,0]}, the average recorded temperature was {annualAvgTempData[i,1]} degrees.')
        print('')

    elif option == 7:
        annualMinTempData = w.getMinTempAnnually()
        years = []
        minTemps = []
        for i in range(30):
            years.append(annualMinTempData[i,0])
            minTemps.append(annualMinTempData[i,1])
        
        c = Chart("Minimum Temperatures annually from 1990-2019", "Year", "Min Temps (Degrees)", years, minTemps)
        c.drawLineChart()

    elif option == 8:
        annualMaxTempData = w.getMaxTempAnnually()
        years = []
        maxTemps = []
        for i in range(30):
            years.append(annualMaxTempData[i,0])
            maxTemps.append(annualMaxTempData[i,1])
        
        c = Chart("Maximum Temperatures annually from 1990-2019", "Year", "Max Temps (Degrees)", years, maxTemps)
        c.drawLineChart()

    elif option == 9:
        annualSnowFallData = w.getAvgSnowFallAnnually()
        years = []
        snowfall = []
        for i in range(30):
            years.append(annualSnowFallData[i,0])
            snowfall.append(annualSnowFallData[i,1])

        c = Chart("Average Snowfall annually from 1990-2019", "Year", "Avg Snowfall (cm)", years, snowfall)
        c.drawBarChart()

    elif option == 10:
        annualAvgTempData = w.getAvgTempAnnually()
        years = []
        temps = []
        for i in range(30):
            years.append(annualAvgTempData[i,0])
            temps.append(annualAvgTempData[i,1])
        
        c = Chart("Average Temperatures annually from 1990-2019", "Year", "Avg Temps (Degrees)", years, temps)
        c.drawBarChart()

    else:
        print("Invalid Choice Inputted")
        print('')

if __name__ == "__main__":
    main()