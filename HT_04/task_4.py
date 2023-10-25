# Write a Python program that demonstrates exception chaining. Create a custom exception class called
# CustomError and another called SpecificError. In your program (could contain any logic you want), raise a
# SpecificError, and then catch it in a try/except block, re-raise it as a CustomError with the original exception
# as the cause. Display both the custom error message and the original exception message.


class CustomError(Exception):
    def __init__(self, err_message, cause):
        super().__init__(err_message)
        self.cause = cause


class SpecificError(Exception):
    def __init__(self, err_message):
        super().__init__(err_message)


try:
    raise SpecificError("Its specific error block  message")
except SpecificError as spec_err:
    try:
        raise CustomError(f"Custom error was called because of raising Specific error", spec_err)
    except CustomError as cust_err:
        print(f"Custom error has dat text : {cust_err}")
        print(f"Original exception was : {CustomError} and dat cause of raising {cust_err.cause}")
