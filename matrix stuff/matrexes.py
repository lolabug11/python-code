import random as r
class Matrex:
    def __init__(self, data:list, width, length):
        self.data = data
        self.width = width
        self.length = length
        self.id = r.randint(1,1000)
        rows = []
        for x in range(self.length):
            start = x * self.width
            end = start + self.width
            rows.append(self.data[start:end])
            rows.append('\n')
            self.rows = rows
        row_data = ''
        for x in self.rows:
            row_data += str(x)
        self.rows = row_data

test = Matrex([1,2,3,4,5,6,7,8,9], 3,3)
print(f'The matrix with the id of {test.id} has data that is \n{test.rows}')