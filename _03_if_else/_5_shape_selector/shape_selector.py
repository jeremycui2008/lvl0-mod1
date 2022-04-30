
import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    bill=turtle.Turtle()
    # Make a new turtle
    shape=simpledialog.askstring(title='what shape', prompt='select a shape you wanna draw')
    # Ask the user what shape they want to draw and store it in a variable
    if shape=='Circle':
        bill.circle(radius=30, steps=30)
    if shape=='triangle':
        bill.right(60)
        bill.forward(100)
        bill.left(120)
        bill.forward(100)
        bill.left(120)
        bill.forward(100)
    if shape=='square':
        for i in range (4):
            bill.forward(100)
            bill.right(90)
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
