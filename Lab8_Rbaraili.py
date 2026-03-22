"""
The program's name: Geometry Calculator
Your name (the author): Rajani Baraili
The purpose of the program: To calculate the area and perimeter/circumference of circles and rectangles by importing functions from separate modules.
Any info about starter code:none
Date: March 22, 2026
"""
import circle
import rectangle

# WHY ALIASES ARE NECESSARY:
# Both circle.py and rectangle.py define a function named area().
# If we imported both modules without aliases, the second import would
# silently overwrite the first module's area() function, making it
# permanently unreachable — Python would not raise any error.
# By using aliases (import circle as c and import rectangle as r),
# we can explicitly call c.area() for circles and r.area() for rectangles,
# allowing both functions to coexist in the same program without conflict.
