#Code by Andrew Howe and John Manoli

import numpy as np

class FileIO:
    def __init__(self):

        self.filepath = "CalgaryWeather.csv"

        self.dataTable = np.loadtxt(self.filepath , delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
 