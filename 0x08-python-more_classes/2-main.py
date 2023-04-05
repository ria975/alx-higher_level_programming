#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(4, 7)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 15
my_rectangle.height = 7
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
