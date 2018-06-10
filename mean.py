from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(17)


testing = numpy.loadtxt("data/testing.csv", delimiter=",")
training = numpy.loadtxt("data/training.csv", delimiter=",")
sum = 0

values = testing[:,6]
values2 = testing[:,6]

for value in values:
    if value != 800:
        sum = sum + value

for value in values2:
    if value != 800:
        sum = sum + value

print (sum/(699-16))
