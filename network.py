import math
import random


class AI:
    def __init__(self, market, weights):
        self.stocks = dict()
        for each in market.keys():
            self.stocks[each] = 0
        self.money = 10000
        if not weights:
            self._weights = [random.random(1.0) for i in range(30)]
        else:
            self._weights = weights

    def train(self, training_input, training_output, loop):
        for i in range(loop):
            for j in range(len(training_input)):
                prediction = self._feedforward(training_input[j])
                self._change_weights(prediction, training_output[j])

    def predict(self, market):
        prediction = dict()
        for company in market.keys():
            prediction[company] = self._feedforward(market[company])
        return prediction

    def _feedforward(self, info):
        input_neurons = info
        z = 0
        for i in range(len(self._weights)):
            z += input_neurons[i] * self._weights[i]
        return 2 / (1 + (math.e ** ((-2) * z))) - 1

    def _change_weights(self, prediction, actual):
        for each in self._weights:
            change = 2*(prediction - actual)*(1 - (2 / (1 + (math.e ** ((-2) * each))) - 1) ** 2) * each
            each += change

    def choice(self, prediction):
        operation = dict()
        for company in prediction.keys():
            if prediction[company] >= 0.9:
                operation[company] = 100
            elif prediction[company] >= 0.8:
                operation[company] = 80
            elif prediction[company] >= 0.7:
                operation[company] = 50
            elif prediction[company] >= 0.6:
                operation[company] = 20
            elif prediction[company] >= 0.5:
                operation[company] = 10
            elif prediction[company] >= 0.4:
                operation[company] = -(self.stocks[company]//4)
            elif prediction[company] >= 0.3:
                operation[company] = -(self.stocks[company]//2)
            else:
                operation[company] = -self.stocks[company]
        return operation
