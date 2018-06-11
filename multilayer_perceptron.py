# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(17)
# load pima indians dataset
#dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
training = numpy.loadtxt("data/training.csv", delimiter=",")
testing = numpy.loadtxt("data/testing.csv", delimiter=",")

# split into input (X) and output (Y) variables
X = training[:,1:10]
Y = training[:,10]

# create model
model = Sequential()
model.add(Dense(15, input_dim=9, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['acc'])
# Fit the model
model.fit(X, Y, epochs=500, batch_size=5)


# split into input (X) and output (Y) variables
X = testing[:,1:10]
Y = testing[:,10]
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print("%s: %.2f" % (model.metrics_names[0], scores[0]))
print("Erro medio: %.4f" % (1 - scores[1]))
