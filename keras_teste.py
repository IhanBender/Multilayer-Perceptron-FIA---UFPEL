from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

# diabetes testing dataset
training = numpy.loadtxt("data/data.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = training[:,0:10]
Y = training[:,10]


model = Sequential()
model.add(Dense(20, input_dim=10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=100, batch_size=5)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print("%s: %.2f" % (model.metrics_names[0], scores[0]))
