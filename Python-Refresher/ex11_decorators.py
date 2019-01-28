# A decorator is a function that gets called before another function

import functools


def my_decorator(func):  # decorator being before another function
    @functools.wraps(func)  # functool to wrap around the function being passed
    def function_that_runs_func():  # function used as wrapper
        print("In the decorator")
        func()  # my_function passed as argument func
        print("After the decorator")
    return function_that_runs_func  # wrap function is returned


@my_decorator  # means function below should be called after my_decorator(arg)
def my_function():  # function that get passed as arg to my_decorator()
    print("I'm the function!")


# my_function()


# A more complex decorator is a decorator that can accept arguments itself
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):  # accepts many arguments
            print("In the decorator!")  # we can do things before
            if number == 56:
                print("Not running the function!")
            else:
                func(*args, **kwargs)  # arguments recieved
            print("After the decorator")  # and can do things after
        return function_that_runs_func
    return my_decorator  # return the decorator


@decorator_with_arguments(57)  # start by defining the decorator with arguments
def my_function_too(arg1, arg2):  # function to pass inside the decorator
    print(arg1 + arg2)


my_function_too(57, 67)

# decorators are mustly used for secirity reasons. For example when asking for
# website credentials. We might want to check the credentials entered before
# serving a webpage. Therefore, function to server the webpage or admin page or
# getting data from database is only called after true authentication.
