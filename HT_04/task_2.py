# Create a custom exception class called NegativeValueError. Write a Python program that takes an integer as input and
# raises the NegativeValueError if the input is negative. Handle this custom exception with a try/except block and
# display an error message.
class NegativeValueError(Exception):
    def __init__(self, number):
        super().__init__(f"Error : your negative number {number} is not allowed")


try:
    x = int(input("Enter pls non negative number "))
    if x < 0:
        raise NegativeValueError(x)

    print(f"Your number {x} is non-negative as was needed ")
except NegativeValueError as e:
    print(e)
