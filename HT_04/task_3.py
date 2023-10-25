# Create a Python script that takes an age as input. If the age is less than 18 or greater than 120, raise
# a custom exception called InvalidAgeError. Handle the InvalidAgeError by displaying an appropriate error message.

class CustomAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Your entered age {age} is out of allowed range")


try:
    age = int(input("Please enter your age in range , allowed age is 18-120 "))
    if not 18 <= age <= 120:
        raise CustomAgeError(age)
    print(f"Your entered age is {age}")
except CustomAgeError as e:
    print(f"AgeError:{e}")
