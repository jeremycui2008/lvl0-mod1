"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
import math
from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    robert = 0
    rob = simpledialog.askinteger(title='number 1', prompt='select a number')
    bob = simpledialog.askinteger(title='number 2', prompt='select another number')
    bill = simpledialog.askstring(title='select a type of equation', prompt='would you like to multiply, divide, add, or subtract?')
    if bill=='multiply':
        robert = rob*bob
    elif bill=='subtract':
        robert = rob-bob
    elif bill=='divide':
        robert = rob/bob
    else:
        robert=rob+bob
    print(robert)



