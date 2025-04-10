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
        if x_as_number > 0 and y_as_number > 0:
            print(
                "The coordinates {}, {} are in quadrant 1.".format(
                    x_as_number, y_as_number
                )
            )
        elif x_as_number < 0 and y_as_number > 0:
            print(
                "The coordinates {}, {} are in quadrant 2.".format(
                    x_as_number, y_as_number
                )
            )
        elif x_as_number < 0 and y_as_number < 0:
            print(
                "The coordinates {}, {} are in quadrant 3.".format(
                    x_as_number, y_as_number
                )
            )
        elif x_as_number > 0 and y_as_number < 0:
            print(
                "The coordinates {}, {} are in quadrant 4.".format(
                    x_as_number, y_as_number
                )
            )
        else:
            print("This point doesn't exist")

    except:
        print("That was not a number.")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
