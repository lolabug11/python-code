class VendingMachine:
    def __init__(self, name):
        self.stock = {}
        self.balance = 0
        self.name = name

    def __str__(self):
        return_string = f'{self.name} has a balance of {self.balance} and has,\n'
        for item in self.stock:
            return_string += f'{item} with {self.stock[item][0]} left in stock,\n'
        return return_string
    def stock_item(self,item:str, price, stock):
        if item not in self.stock:
            self.stock[item] = [stock, price]
        else:
            self.stock[item][0] += stock

    def buy(self, item):
        if item in self.stock:
            if self.stock[item][0] > 0:
                self.stock[item][0] -= 1
                self.balance += self.stock[item][1]
            else:
                print(f'{self.name} does not have any {item} left in stock.\n Sorry for the inconvenience')

        else:
            print(f'Sorry for the inconvenience but {self.name} does not have {item} in stock.')

    def remove_item_from_stock(self, item):
        if item in self.stock:
            del self.stock[item]
        else:
            print(f'{item} was never in stock at {self.name}')

    def is_available(self, item):
        if item  in self.stock :
            if self.stock[item][0] > 0 :
                print(f'{item} is in stock at {self.name}')
            else:
                print(f'{item} is not in stock at {self.name}')
        else:
            print(f'{item} is not in stock at {self.name}')


walmart_vm = VendingMachine('Walmart vending machine')

walmart_vm.stock_item('Cheetos', 1.00, 10)
walmart_vm.stock_item('Doritos', 1.25, 10)
print(walmart_vm)
walmart_vm.buy('Cheetos')
print(walmart_vm)
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
walmart_vm.buy('Cheetos')
print(walmart_vm)
walmart_vm.stock_item('Cheetos', 1.00, 100)