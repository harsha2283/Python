#custom exception creation
class CustomExceptionHarshaMade(Exception):
    pass

x = 2  # comment this to see the Exception error (NameError)

try:
    raise CustomExceptionHarshaMade("This is Custom created Exception!\nGo Make your own Exception")
    # print(x/0) # uncomment this to see the exception error (ZeroDivisionError)

    # if not type(x) is str: # uncomment this to see the custom data for the builtin errors
    #     raise TypeError(" - Only strings are expected to be passed")
except ZeroDivisionError:
    print("- Please don't divide anything with zero")
except NameError:
    print("- something is probably not defined properly or not defined at all")
except Exception as error:
    print(error)
else:
    print("- No Exceptions are raised")
finally:
    print("This gets passed when there is no exception and exceptions are raised")