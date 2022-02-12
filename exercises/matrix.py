class Matrix(object):
    def __init__(self, name,value = [], dimensions = None ):
        self.name = name
        self.value = value
        self.dimensions = dimensions
        

    def creatematrix(self, i , j):
        x = 0
        y = 0
        while x < i:
            self.value.append([])
            y = 0
            while y < j:
                submat = int(input("Enter value of " + self.name + str(x+1) + str(y+1) + ": "))
                self.value[x].append(submat)
                y += 1

            x += 1

        self.dimensions = str(i) + '*' + str(j)

        return self.value

    def resetmatrix(self):
        self.value = []
        self.dimensions = None

        return self.value


    def addmatrix(self , b_matrix):
        if self.dimensions == None or b_matrix.dimensions == None:
            return False
        elif self.dimensions != b_matrix.dimensions:
            return False
        else:
            addmat = []
            i = 0
            while i < len(self.value):
                j = 0
                addmat.append([])
                while j < len(self.value[i]):
                    addmat[i].append(self.value[i][j] + b_matrix.value[i][j])
                    j += 1
                i += 1

            return addmat


                        




a = Matrix('a')
b = Matrix('b')
a.creatematrix(2,2)
print(a.value)
print(b.value)




            


        