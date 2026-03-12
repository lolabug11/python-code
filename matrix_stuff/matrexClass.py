import random as r
class Matrex:

    def __init__(self, data:list, row, col):
        self.data = data
        self.col = col
        self.row = row
        self.id = r.randint(1,1000)


    def __str__(self):
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
        return row_data
        
    def add(self,other):
        if isinstance(other,Matrex):
            
            if self.check_dimentions(other):
                new_matrex = []
                for x in range(len(self.data)):
                    new_matrex.append(self.data[x] + other.data[x])
                return Matrex(new_matrex,self.row,self.col)
            else:
                raise TypeError('Matrex sizes must match to add')

        else:
            raise TypeError("Other muust be matrex")

            
    def subtract(self,other):
        if isinstance(other,Matrex):
            
            if self.check_dimentions(other):
                new_matrex = []
                for x in range(len(self.data)):
                    new_matrex.append(self.data[x] - other.data[x])
                return Matrex(new_matrex,self.row,self.col)
            else:
                print('The matrexs are not the same size')


    def scalar_multiply(self, scalar):
        new_data = []
        for x in range(len(self.data)):
            new_data.append(self.data[x] * scalar)
        return Matrex(new_data,self.row,self.col)
    

    def is_equal(self, other):
        if isinstance(other,Matrex):
            if self.col == other.col and self.row == other.row:
                for x in range(len(self.data)):
                    if abs(self.data[x] - other.data[x]) > 0.0000001:
                        return False
                return True
        else:
            return False


    def transpose(self):
        new_col = self.row
        new_row = self.col
        new_data = []
        for c in range(self.col):
            for r in range(self.row):
                spot = c + (r*self.col)
                new_data.append(self.data[spot])

        return Matrex(new_data, new_row, new_col)
    

    def copy(self):
        new_data = self.data[:]
        return Matrex(new_data,self.row,self.col)
    
    def is_square(self):
        if self.col == self.row:
            return True
        else:
            return False
    

    def shape(self):
        return (self.row, self.col)
            




    def check_dimentions(self, other):
        return self.row == other.row and self.col == other.col
# [a,b,c] [r,s,t]   [(ar+bu+cx), (as+bv+cy), (at+bw+cz)]
# [d,e,f]*[u,v,w] = [(dr+eu+fx), (ds+ev+fy), (dt+ew+fz)]
# [g,h,i] [x,y,z]   [(gr+hu+ix), (gs+hv+iy), (gt+hw+iz)]
    def multiply(self, other):
        if isinstance(other,Matrex):
            if self.col == other.row:
                row_count = self.row
                col_count = other.col
                new_data = []
                for r in row_count:
                    for c in col_count:
                        new_data.append(sel)


            else:
                raise TypeError
        else:
            raise TypeError
            
    @staticmethod
    def zero_matrex(row,col):
        data = []
        for r  in range(row):
            for c  in range(col):
                data.append(0)
        return Matrex(data, row, col)