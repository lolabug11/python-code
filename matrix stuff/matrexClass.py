import random as r
class Matrex:

    def __init__(self, data:list, col, row):
        self.data = data
        self.col = col
        self.row = row
        self.id = r.randint(1,1000)
        matrex = []
        for x in range(self.row):
            start = x * self.col
            end = start + self.col
            matrex.append(self.data[start:end])
            matrex.append('\n')
            self.matrex = matrex
        row_data = ''
        for x in self.matrex:
            row_data += str(x)
        self.matrex = row_data


        
    def add(self,other):
        if isinstance(other,Matrex):
            
            if self.col == other.col and self.row == other.row:
                new_matrex = []
                for x in range(len(self.data)):
                    new_matrex.append(self.data[x] + other.data[x])
                return Matrex(new_matrex,self.col,self.row)
            else:
                raise TypeError('Matrex sizes must match to add')

        else:
            raise TypeError("Other muust be matrex")

            
    def subtract(self,other):
        if isinstance(other,Matrex):
            
            if self.col == other.col and self.row == other.row:
                new_matrex = []
                for x in range(len(self.data)):
                    new_matrex.append(self.data[x] - other.data[x])
                return Matrex(new_matrex,self.col,self.row)
            else:
                print('The matrexs are not the same size')


    def scalar_multiply(self, scalar):
        new_data = []
        for x in range(len(self.data)):
            new_data.append(self.data[x] * scalar)
        return Matrex(new_data,self.col,self.row)
    

    # def multiply(self,other):
    #     if isinstance(other, Matrex):
    #         if self.col == other.row:
    #             new_data = []
    #             if self.col  == other.row:
    #                 pass
    def is_equal(self, matrex2):
        if isinstance(matrex2,Matrex):
            if self.col == matrex2.col and self.row == matrex2.row:
                for x in range(len(self.data)):
                    if abs(self.data[x] - matrex2.data[x]) > 0.0000001:
                        return False
                return True
        else:
            return TypeError


    def transpose(self):
        for x in range(self.row):
            #TODO
            pass