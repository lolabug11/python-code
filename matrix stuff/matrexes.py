class Matrex:
    def __init__(self, data:list, width, length):
        self.data = data
        self.width = width
        self.length = length

        rows = {}
        for x in range(self.length):
            start = x * self.width
            end = start + self.width
            rows[f'row{x+1}'] = self.data[start:end]
            self.rows = rows
test = Matrex([1,2,3,4,5,6,7,8,9], 3,3)
print(test.rows)