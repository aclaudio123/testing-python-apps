# A dictionary is a Key-value set which allows us to store data
# It's a set so unordered, and stores only unique elements

# set
my_set = {1, 3, 5}

# dictionary are key-value elements
# keys must be immutable; strings, integer, tuples people_without_spaces

my_dict = {'name': 'Jose', 'age': 90, 'grades': [14, 35, 67, 90]}

# tuples within a dictionary
lottery_player = {
    'name': 'John',
    'numbers': (13, 45, 66, 34, 22)
}

# dictionary inside a list
universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

# calculate sum of lottery_player's numbers
sum(lottery_player['numbers'])

# change the value of a key
lottery_player['name'] = 'John'
my_dict['grades'][0] = 25  # 'grades': [24, 35, 67, 90]

lottery_player['numbers'][0] = 25  # is will fail bcos tuples are immutable


# =============== Exercise ==================================
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values
# 66, 77, and 88.
student = pass

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data
# dictionary.


def average_grade(data):
    grades =   # Change this!
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average
# grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here
        pass

    return total / count
