

# passing a function is function is a paradigm known as
# declearative programming or functional programming.
# It's especially usedful when we working with data
# passing a function as argument to another function
# argument name = arg1
def methodception(arg1):
    # return arg1 as a function, arg1()
    return arg1()


def add_two_numbers():
    return 35 + 77


# pass the method as a paramenter without () at the end
print(methodception(add_two_numbers))

# ======== Lambda functions =================================
# A lambda function is an anonymous function.
# lambda functions are written in one line
print(methodception(lambda: 35 + 77))  # same output as above


# Exercise: Find all the elements in the list below that are not 13

my_list = [13, 56, 77, 484]

# we can do this in many ways

# 1. using Python built-in filter() function
# ============= filter() =======================
# filter() method is built-in method that let's you keep only some values
# It takes two params; a function and iterable -- filter(function, iterable)
# Most often, a lambda function is used as the filer function since lambda
# is a oneliner function. however, you can create you own function and pass it.

new_list = filter(lambda x: x != 13, my_list)
# the function reads as get all f(x) such that x != 13 from my_list

print(list(new_list))  # need to wrap with list() to return values as a list


# same as
def not_thirteen(x):
    return x != 13


print(list(filter(not_thirteen, my_list)))


# 2. using list comprehension
# items of performance, list comprehension is slightly better
new_list2 = [x for x in my_list if x != 13]
print(new_list2)
