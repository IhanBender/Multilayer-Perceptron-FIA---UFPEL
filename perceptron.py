import random
import numpy

class Perceptron:

    def __init__(self, delta = 0.5):
        self.w1 = 0
        self.w2 = 0
        self.theta = 0
        self.delta = delta


    def net(self, x1, x2):
       return self.w1 * x1 + self.w2 * x2 + self.theta


    def fNet(self, net):
        if net >= 0.5:
            return 1
        return 0

    # dataset must be a numpy matrix
    def train(self, dataset, eta=0.1, threshold=(1 * 10**(-3)) ):

        numCol = dataset.shape[1]       # gets the number of columns of the dataset
        numRows = dataset.shape[0]      # gets the number of rows (number of training cases)

        self.w1 = random.uniform(-0.5, 0.5)
        self.w2 = random.uniform(-0.5, 0.5)
        self.theta = random.uniform(-0.5, 0.5)

        # answers recebe apenas as respostas
        answers = dataset[:,numCol-1]

        # gets all the parameters column numbers, to find out what are the parameters
        questIndex = []
        for i in range(0, numCol):
            questIndex.append(i)
        # questions receives the parameters
        questions = dataset[:, questIndex]

        # Begins training
        sqError = 2 * t,
        while sqError > threshold:
            sqError = 0.0
            for i in range(0, numRows):
                x1 = questions[i][0]
                x2 = questions[i][1]
                net = self.net(x1, x2)
                fNet = self.fNet(net)

                error = answers[i] - fNet
                sqError = sqError + error**2

                self.w1 = self.w1 - eta*(2*(error) * (-x1))
                self.w2 = self.w2 - eta*(2*(error) * (-x2))
                self.theta = self.theta - eta*(2*(error) * (-1))
            sqError = sqError/numRows
            print sqError


    def run(self, dataset):
        numCol = dataset.shape[0]
        answers = []

        for i in range(0, numCol):
            answers.append(self.fNet(self.net(dataset[i][0], dataset[i][1])))

        print answers
