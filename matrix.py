class Matrix:
    def __init__(self, rows,cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [None]*self.rows
        for i in range(0,self.rows,1):
            self.matrix[i] = [0] * self.cols
    
    def multiply(self, n):
        if(type(n) is Matrix):
            if(self.cols == n.rows and self.rows == n.cols):
                
                result = Matrix(self.rows, n.cols)
                a = self
                b = n

                for i in range(self.rows):
                    for j in range(self.cols):
                        sum = 0
                        for k in range(a.cols):
                            
                            sum += a.matrix[i][k] * b.matrix[k][j]
                            print(sum)
                        result.matrix[i][j] = sum

                return result.matrix
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] *= n
    
    def add(self, n):
        if(type(n) is Matrix):
            if(n.cols == self.cols and n.rows == self.rows ):
                for i in range(self.rows):
                    for j in range(self.cols):
                        self.matrix[i][j] += n.matrix[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n

m1 = Matrix(2,3)
m2 = Matrix(3,2)


m1.matrix[0][0] = 1
m1.matrix[0][1] = 2
m1.matrix[0][2] = 3


m1.matrix[1][0] = 4
m1.matrix[1][1] = 5
m1.matrix[1][2] = 6

m2.matrix[0][0] = 7
m2.matrix[0][1] = 8
m2.matrix[1][0] = 9
m2.matrix[1][1] = 10
m2.matrix[2][0] = 11
m2.matrix[2][1] = 12


print(m1.multiply(m2))



