#Code by Andrew Howe and John Manoli

import numpy as np

array = np.random.randint(100, size = 10)

print (array)

print ("The min is {} \nthe max is {} \nthe average is {} \nthe median is {} \nthe standard deviation is {}.".format (np.min(array), np.max(array), np.average(array), np.median(array), np.std(array)))