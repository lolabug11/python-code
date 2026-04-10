from state_change_class import *
from time import sleep
from human_class import *
class VendingMachine:
    def __init__(self, name):
        self.stock = {}
        self.balance = 0
        self.name = name
        self.state_machine = States('idle')
        self.state_machine.add_state('money_inserted')
        self.state_machine.add_state('dispensing')
        self.state_machine.add_state('returning_change')
        self.state_machine.add_transition('idle', 'insert_money', 'money_inserted')
        self.state_machine.add_transition('money_inserted', 'select_item', 'dispensing')
        self.state_machine.add_transition('money_inserted', 'cancel', 'returning_change')
        self.state_machine.add_transition('dispensing', 'dispense_done', 'idle')
        self.state_machine.add_transition('returning_change', 'change_returned', 'idle')

    def __str__(self):
        return_string = f'{self.name} has made a total of ${self.balance} and has,\n'
        for item in self.stock:
            return_string += f'{item} with {self.stock[item][0]} left in stock,\n'
        return return_string

    def stock_item(self,item:str, price, stock):
        if item not in self.stock:
            self.stock[item] = [stock, price]
        else:
            self.stock[item][0] += stock

    def buy(self, person:Human):
        self.state_machine.trigger('insert_money')
        item = input('What item do you want to buy?\n>')
        sleep(0.5)
        if item in self.stock:
            cancel = input(f'{item} cost ${self.stock[item][1]}. Do you want to cancel this purchase?\n>')
            if 'y' in cancel.lower():
                self.state_machine.trigger('cancel')
                sleep(0.5)
                self.state_machine.trigger('change_returned')
                print('Your change has been returned please collect it before you leave.')
            else:
                if self.stock[item][0] > 0:
                    if person.balance >= self.stock[item][1]:
                        self.state_machine.trigger('select_item')
                        self.stock[item][0] -= 1
                        person.balance -= self.stock[item][1]
                        self.balance += self.stock[item][1]
                        self.state_machine.trigger('dispense_done')
                        sleep(0.5)
                        print(f'Your {item} has been dispensed thank you for your purchase today!')
                    else:
                        print(f'You dont have enough money to buy {item}.')
                        self.state_machine.trigger('cancel')
                        sleep(0.5)
                        self.state_machine.trigger('change_returned')
                else:
                    self.state_machine.trigger('cancel')
                    sleep(0.5)
                    self.state_machine.trigger('change_returned')
                    print(f'{self.name} does not have any {item} left in stock. Your change has been returned please collect it before you leave.\n Sorry for the inconvenience.')
        else:
            self.state_machine.trigger('cancel')
            sleep(0.5)
            self.state_machine.trigger('change_returned')
            print(f'Sorry for the inconvenience but {self.name} does not have {item} in stock. Your change has been returned please collect it before you leave.')

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







