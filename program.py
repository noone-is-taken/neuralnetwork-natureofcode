from random import random


class Perceptron:
    
    def __init__(self):
        self.weight = [random(),random()]
        self.lr = 0.1

    def guess(self,inputs):
        sume = 0
        for i in self.weight:
            sume += inputs[i] * self.weight[i]
        return sign(sume)

    def train(self,inputs,target):
        guess = self.guess(inputs)
        error = target - guess

        for i in self.weight:
            self.weight[i] += error * inputs[i] * self.lr


def sign(n):
    if(n>=0):
         return 1
    else:
         return 0


class Point:
    def __init__(self):
        self.x = random()*10
        self.y = random()*10
        if self.x > self.y:
            self.label = 1
        else: 
            self.label = -1