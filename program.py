from random import random


class Perceptron:
    
    def __init__(self):
        self.weight = [random(),random()]
        self.lr = 0.1

    def guess(self,inputs):
        sume = 0
        for i in range(len(self.weight)):
            sume += inputs[i] * self.weight[i]
        return sign(sume)

    def train(self,inputs,target):
        guess = self.guess(inputs)
        error = target - guess
        
        for i in range(len(self.weight)):
            self.weight[i] += error * inputs[i] * self.lr


def sign(n):
    if(n>=0):
         return 1
    else:
         return -1


class Point:
    def __init__(self):
        self.x = random()*10
        self.y = random()*10
        if self.x > self.y:
            self.label = 1
        else: 
            self.label = -1



neuron = Perceptron()
points = []
for i in range (10):
    points.append(Point())

print(neuron.weight)

for i in range(len(points)):
    inputs = [points[i].x, points[i].y]
    print(points[i].x," ",points[i].y, " ",points[i].label, "guess: ",neuron.guess(inputs))

for k in range(100):
    for i in range(len(points)):
        inputs = [points[i].x, points[i].y]
        neuron.train(inputs,points[i].label)
print("---------")
for i in range(len(points)):
    inputs = [points[i].x, points[i].y]
    print(points[i].x," ",points[i].y, " ",points[i].label, "guess: ",neuron.guess(inputs))


print(neuron.weight)