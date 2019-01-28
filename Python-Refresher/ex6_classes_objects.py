# dictionary can't do anything on it's own data
# it can't do any operations with it's own data
lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}


# objects
# A class is a blueprint or template
# Our class tells us what a lottery player has
class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


# create an object or instance of the class
# the object can have actions or methods associated with it
# player_one and player_two are two different entities that share the
player_one = LotteryPlayer('John')
player_two = LotteryPlayer('Jose')

print(player_one.name)  # John
print(player_one.total())  # sum((5, 9, 12, 3, 1, 21))

# change player_one numbers
player_one.numbers = (1, 2, 3, 6, 7, 8)  # replacing old numbers with new one

print(player_one.numbers == player_two.numbers)  # False


# class should always have an __init__ method
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return sum(self.grades) / len(self.grades)

    # creating a staticmethod (method without self as argument)
    @staticmethod   # method that doesn't recieve an implicite first argument
    def go_to_school():  # no self bcos print statement is generic
        print("I'm going to school")

    # create a @classmethod (method with cls as first argument)
    # using same method name for demo
    @classmethod   # this means we'll pass class name Student as our argument
    def going_to_school(cls):  # @classmethod argument holder is cls
        print("Not going to school")  # same to all object calling the method
        print("I'm a {}".format(cls))


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")

anna.grades.append(56)
anna.grades.append(71)
print(anna.grades)  # [56, 71]

# print Anna's avg grade
# Note: only time we really need to use the object to call a method is when the
# method has an implicite first argument self
print(anna.average())


# =========== Methods withous self in them =====================
# method has to be declared as @staticmethod or @classmethod

# calling @staticmethod and @classmethod using the objects
anna.go_to_school()  # @staticmethod prints I'm going to school
rolf.go_to_school()  # prints same thing

anna.going_to_school()  # @classmethod prints 'Not going to school'
rolf.going_to_school()  # prints same thing

# calling the @staticmethod and @classmethod by using the class name
# since it doesn't matter which object calls the methods we get generic output
# therefore we can just used the class name Student as the object.
Student.go_to_school()  # prints I'm going to school
Student.going_to_school()  # prints 'Not going to school'


# ============== Exercise ==================================
class Store:
    def __init__(self):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items'
        # to be an empty list.
        pass

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to
        # self.items.
        pass

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
