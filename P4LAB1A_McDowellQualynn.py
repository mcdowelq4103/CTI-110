# Qualynn McDowell
# November 6, 2026
# P4LAB1A
# Uses turtle and loops to draw a square and a triangle.

# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set up the turtle window and pen
win.title('House of Graphics')
win.bgcolor("skyblue")

pen.pensize(5)
pen.color("darkgreen")
pen.shape("arrow")

# Code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.right(90)

# Wile loop that executes 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides -= 1

# Close the turtle window when clicked
win.mainloop()