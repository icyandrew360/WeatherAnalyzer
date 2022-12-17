#Code by Andrew Howe and John Manoli

import numpy as np

from FileIO import FileIO

from TemperatureData import TemperatureData

from Date import Date

from Chart import Chart

import matplotlib.pyplot as pyplot

f = FileIO()

t = TemperatureData()

d = Date()


class WeatherAnalyzer:
    def __init__(self):
        self.minTemps = [] #appending all min temps recorded to an empty array
        self.maxTemps = []
        self.minTemps.append(t.minTemperature)
        self.maxTemps.append(t.maxTemperature)

    def getMinTemp(self):
     
        minTemp1=np.min(self.minTemps) #This is the lowest temperature out of the data set
        IndexMin = np.argmin(self.minTemps) #This gives us the index number of the lowest temp in the data set
        fullMinTempData = [minTemp1, d.year[IndexMin], d.month[IndexMin]]  #For all of the data, this array contains the lowest recorded temp,
        return fullMinTempData                                                                                                #the year and month that it happened.


  
    def getMinTempAnnually(self):
        SeperateMinTemps = [] #This will be the array of ONLY the min temps of each year
        Temp1 = [] #temporary arrays to hold data
        Temp2 = []
        MinTempYearly = []  #This array will hold Year, min temp, year, min temp etc. Will be arranged to be 2d later.
        for i in range (348):
            Temp1.append(t.minTemperature[i]) #holding every value of min temperature up to 2019
        for i in range (348,359):
            Temp2.append(t.minTemperature[i]) #holding values of min temperature for 2019

        Temp1 = np.array(Temp1).reshape(29,12) #Creating 2d numpy array to show all min temps for each year
        Temp2 = np.array(Temp2) #turning 2019 into numpy array

        for i in range (29):
            SeperateMinTemps.append(np.min(Temp1[i])) #Taking the minimum value from each year, putting it into the other array

        SeperateMinTemps.append(np.min(Temp2)) #adding the minimum value from 2019
        
        for i in range (30):
            MinTempYearly.append(d.SeperateYears[i])
            MinTempYearly.append(SeperateMinTemps[i])
        
        MinTempYearly = np.array(MinTempYearly).reshape(30,2)

        return MinTempYearly



    def getMaxTemp(self):
       
        maxTemp1=(np.max(self.maxTemps))
        IndexMax = np.argmax(self.maxTemps)
        fullMaxTempData = [maxTemp1, d.year[IndexMax], d.month[IndexMax]] #just in case we need the values in an array

        return (fullMaxTempData)

    def getMaxTempAnnually(self):
        SeperateMaxTemps = []
        Temp1 = []
        Temp2 = []
        MaxTempYearly = []
        for i in range (348):
            Temp1.append(t.maxTemperature[i])
        for i in range (348,359):
            Temp2.append(t.maxTemperature[i])

        Temp1 = np.array(Temp1).reshape(29,12)
        Temp2 = np.array(Temp2)

        for i in range (29):
            SeperateMaxTemps.append(np.max(Temp1[i]))

        SeperateMaxTemps.append(np.max(Temp2))
        
        for i in range (30):
            MaxTempYearly.append(d.SeperateYears[i])
            MaxTempYearly.append(SeperateMaxTemps[i])
        
        MaxTempYearly = np.array(MaxTempYearly).reshape(30,2)

        return MaxTempYearly



    def getAvgSnowFallAnnually(self):
        AverageSnowFall = []
        Temp1 = []
        Temp2 = []
        SnowFallYearly = []
        for i in range (348):
            Temp1.append(t.snowFall[i])
        for i in range (348,359):
            Temp2.append(t.snowFall[i])

        Temp1 = np.array(Temp1).reshape(29,12)
        Temp2 = np.array(Temp2)

        for i in range (29):
            AverageSnowFall.append(np.average(Temp1[i]))

        AverageSnowFall.append(np.average(Temp2))
        
        for i in range (30):
            SnowFallYearly.append(d.SeperateYears[i])
            SnowFallYearly.append(AverageSnowFall[i])
        
        SnowFallYearly = np.array(SnowFallYearly).reshape(30,2)

        return SnowFallYearly

    def getAvgTempAnnually(self):
        AverageTemps = []
        Temp1 = []
        Temp2 = []
        AvgTempYearly = []
        for i in range (696):
            Temp1.append(t.avgTemperature[i])
        for i in range (696, len(t.avgTemperature)):
            Temp2.append(t.avgTemperature[i])
        
        Temp1 = np.array(Temp1).reshape(29,24)
        Temp2 = np.array(Temp2)

        for i in range (29):
            AverageTemps.append(np.average(Temp1[i]))

        AverageTemps.append(np.average(Temp2))

        for i in range(30):
            AvgTempYearly.append(d.SeperateYears[i])
            AvgTempYearly.append(AverageTemps[i])

        AvgTempYearly = np.array(AvgTempYearly).reshape(30,2)
        
        return AvgTempYearly
        
# def main():
#     w = WeatherAnalyzer()
#     #w.getMinTempLineChart()

# if __name__ == "__main__":
#     main()
 