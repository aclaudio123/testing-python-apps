my_variable = "hello"

# for loop
# my_variable is called an iterable
for character in my_variable:  # iterables are strings, list, tuples, and more
    print(character)

my_list = [1, 3, 5, 7, 9]

for number in my_list:
    print(number ** 2)


# while loop
# used when you want to keep repeating something to be done
user_wants_number = True
while user_wants_number is True:
    print(10)
    user_input = input("should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False


# ============= if statements ================================
# If statements
should_continue = True
if should_continue:
    print("Hello")

known_people = ["John", "Anna", "Mary"]
person = input("Enter a person you know: ")

if person in known_people:
    print("You know {}!".format(person))
else:
    print("You don't know {}!".format(person))


# =============== Exercise ==================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        evens.append(number)
    return evens


# Modify the below method so that "Quit" is returned if the choice parameter
# is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"


# Exercise 2
def who_do_you_know():
    # Ask the user for a list of people they known
    # split the string into a list
    # Return that list
    people = input("Enter names of people you know, separated by commas: ")
    people_list = people.split(",")

    # remove any whitespaces
    people_without_spaces = [person.strip() for person in people_list]

    return people_without_spaces


def ask_user():
    # Ask user for a name
    # See if the name is in the list of people they know
    # Print out that they know the person
    name = input("Enter a name: ")
    if name in who_do_you_know():
        print("You know {}!".format(name))
    else:
        print("You don't know {}!".format(name))


ask_user()
