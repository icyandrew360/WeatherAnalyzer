#Code by Andrew Howe and John Manoli

import numpy as np


def read_weather():
    file_name = "weather.csv"

    data = np.loadtxt(file_name , delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
    
    return data
    



import matplotlib.pyplot as pyplot

def drawChart(x, y):

    fig = pyplot.figure()
    pyplot.title('Temperatures in Calgary between Jan-Dec in 2000')
    pyplot.ylabel('Min Temperature (F)')
    pyplot.xlabel("Month of Year")

    pyplot.plot(x, y, marker='o')
    pyplot.show()

class List():
    def __init__(self, data):
        self.data = data

def main():
    data = read_weather()
    x=[]
    y=[]
    for i in range (12):
        y.append(data[i,3])
    for i in range (12):
        x.append(data[i,1])
    print (x)
    drawChart(x, y)
    

if __name__ == "__main__":
    main()
