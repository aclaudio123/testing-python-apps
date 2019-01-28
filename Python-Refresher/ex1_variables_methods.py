#  Variables

a = 5
b = 10
my_variable = 56
any_variable_name = 10

string_variable = "hello"
single_quotes = 'strings can have single quotes'

# Exercise 1:
# Create two variables, var1 and var2, both with the same value.
# Create two variables, num1 and num2, which multiply together to give 16.


# Methods

def my_print_method(my_argument):
    print(my_argument)


my_print_method()


def my_multiply_method(number_one, number_two):
    return number_one * number_two


result = my_multiply_method(5, 3)
my_print_method(result)

# can also pass my_multiply_method(5, 3) as argument to my_print_method()
# However, this way is not the best since it makes code nit easy to read
my_print_method(my_multiply_method(5, 3))


# Exercise 2:
# Complete the method by making sure it returns 42. .
def return_42():
    # Complete method here
    pass  # 'pass' just means "do nothing". Make sure to delete this!

# Create a method below, called my_method, that takes two arguments and returns
# the result of its two arguments multiplied together.
