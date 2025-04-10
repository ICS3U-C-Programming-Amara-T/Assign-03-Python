#!/usr/bin/env python3

# Created By: Amara Tie

# Date: April 1, 2025

# This is a program that finds out what quadrant each coordinate lies 

def main():
    # Greeting
    print("Hello! Let's find the quadrant of a coordinate!")

     # Ask user for x and y coordinates
    x_as_string = input("Enter the x coordinate: ")
    y_as_string = input("Enter the y coordinate: ")
    print("")

    # Check which quadrate the coordinate resides
    try:
        x_as_number = int(x_as_string)
        y_as_number = int(y_as_string)
