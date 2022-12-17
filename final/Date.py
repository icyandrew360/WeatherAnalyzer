#Code by Andrew Howe and John Manoli

import numpy as np

from FileIO import FileIO

f = FileIO()

class Date:
    def __init__(self):
        self.month = []
        self.year = []
        
        for i in range (len(f.dataTable)):
            self.month.append(f.dataTable[i,1])


        self.SeperateYears = []
        for i in range (len(f.dataTable)):

            while i%12 == 0:   #because the index of the first year is 0, we take every year where the index is divisible by 12
                                                                            # to get the first instance of each year in the array
                self.SeperateYears.append(f.dataTable[i,0])
                i += 1
        for i in range (len(f.dataTable)):
            self.year.append(f.dataTable[i,0])

    


# def main():
#     d = Date()



# if __name__ == "__main__":
#     main()