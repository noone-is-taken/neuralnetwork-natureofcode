class Matrix:
    def __init__(self, rows,cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [None]*self.rows
        for i in range(0,self.rows,1):
            self.matrix[i] = [0] * self.cols
    
    def multiply(self, n):
        if(type(n) is Matrix):
            print("to do work")
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] *= n
    
    def add(self, n):
        if(type(n) is Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n.matrix[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n

m1 = Matrix(3,5)
m2 = Matrix(3,5)

m1.add(2)

m2.add(5)

m1.add(m2)

print(m1.matrix)