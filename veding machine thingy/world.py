from human_class import * 
from vending_machine_class import *
def main():
    school_vm = VendingMachine('school vending machine')
    school_vm.stock_item('Doritos',1.5,10)
    school_vm.stock_item('Lays',1.5,10)
    school_vm.stock_item('M&Ms',2,10)
    school_vm.stock_item("Hershey's ",2,10)
    school_vm.stock_item('Twix',2,10)
    school_vm.stock_item('Snickers',2,10)
    school_vm.stock_item('Doritos',2,10)
    school_vm.stock_item('Pepsi',2.5,10)
    school_vm.stock_item('Coke',2.5,10)
    school_vm.stock_item('Root Beer',2.5,10)
    school_vm.stock_item('Dr.Pepper',2.5,10)
    school_vm.stock_item('Water',1,10)
    school_vm.stock_item('Arizona Icead Tea',1,10)

    jeff = Human('jeff','male')
    jeramy = Human('jeramy', 'male')
    jaxon = Human('jaxon', 'male')
    emma = Human('emma', 'female')
    isable = Human('isable', 'female')
    pepper = Human('pepper', 'female')

    school_vm.buy(emma)
if __name__ == '__main__':
    main()
