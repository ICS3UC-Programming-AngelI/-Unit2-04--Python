#!/usr/bin/env python3
# Created By: Angel
# Date: March 03,2025
# This program asks the user for the radius
# of a circle. It the calculates the area and
# circumference of a circle.


import math


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculates the perimeter and area
    circumference = math.pi * radius * 2
    area = math.pi * radius**2

    # display the circumference and area
    print("")
    print("Area = {} cm^2", format(area))
    print("circumference = {}cm".format(circumference))


if __name__ == "__main__":
    main()
