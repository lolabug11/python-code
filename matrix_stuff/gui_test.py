import tkinter as tk
from matrexClass import *
def main():
    calculator = tk.Tk()
    calculator.title('Calculator')
    calculator.mainloop()
    calculator.geometry('400x400')
    calculator.loadtkinter() 
    calculator.create_matrex = tk. Button(calculator, text = 'create a matrex', command= Matrex() )
if __name__ == '__main__':
    main()