from random import random
from random import uniform


class Perceptron:
    
    def __init__(self):
        self.weight = [random(),random(),random()]#[1.4594698422574401, -1.4929581195187729] or [0.40330356803967315, -0.49735085687041586]
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
    
    def guessY(self, x):
        w0 = self.weight[0]
        w1 = self.weight[1]
        w2 = self.weight[2]
        return -(w2/w1) - (w0/w1)* x


def sign(n):
    if(n>=0):
         return 1
    else:
         return -1


class Point:
    def __init__(self):
        self.x = uniform(-1,1)
        self.y = uniform(-1,1)
        self.bias = 1
        lineY = f(self.x)
        if self.y > lineY:
            self.label = -1
        else: 
            self.label = 1

def f(x):
    #y=mx+b
    return 0.3*x+2

neuron = Perceptron()
points = []
for i in range (10):
    points.append(Point())

points[0].x = 0
points[0].y = 0
print(neuron.weight)
it = 0
correct = 0
for i in range(len(points)):
    it += 1
    inputs = [points[i].x, points[i].y,points[i].bias]#the bias is always 1
    if(points[i].label == neuron.guess(inputs)):
        correct += 1
        
print((correct/it)*100,"%")
for k in range(10):
    for i in range(len(points)):
        inputs = [points[i].x, points[i].y, points[i].bias]#the bias is always 1
        neuron.train(inputs,points[i].label)
        #print("the real y: ",f(1),"the guess y: ",neuron.guessY(1))
    

correct = 0
it = 0
for i in range(len(points)):
    it += 1
    inputs = [points[i].x, points[i].y, points[i].bias]#the last 1 is the bias
    if(points[i].label == neuron.guess(inputs)):
        correct += 1
        
print((correct/it)*100,"%")

print(neuron.weight)