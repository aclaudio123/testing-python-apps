# =================== *args and **kwargs ========================
# *args means many arguments can be passed (placeholder for many args)
# **kwargs (placeholder for many keyword arguments; fn='John', ln='Smith' etc)


# Examples
def my_addition(*args):
    # returns sum of all args help by placeholder (*args)
    return sum(args)


total = my_addition(15, 24, 33, 46, 50, 85, 6)
print(total)


# **kwargs = placeholder for many key-values
# returns a dictionary of key-value pairs
def what_are_kwargs(**kwargs):
    return(kwargs)


kw = what_are_kwargs(name='John', school='Oxford', location='UK')
print(kw)


# =============== How we can use them in our programs ===============
# we can use *args and **kwargs in situations where we don't know how many
# values will be passed. Therefore no matter how many are passed, hold them
# all.
# Example: our inheritance program below
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod  # converts a function to a class method
    # Here we can use *args and/or **kwargs to hold any kind of arguments
    # This means we don't have to change our @classmethod implementation
    # when any of our class __init__ definition changes. For example,
    #  WorkingStudent __init__ has added more arguments than in inheritance.py
    # (name, school, salary, job_title, location):
    # we can use *args and **kwargs to hold any format they passed as.
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)

    # This means any arguments not key-value pairs will be stored in *args
    # while all key-value pairs will be stored in **kwargs
    # 1. (**kwargs) salary=17.50, job_title='Engineer', location='US'
    # 2. (*args, **kwargs) 17.5, 'Engineer', location='US'


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title, location):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title
        self.location = location


# WorkingStudent object must have same number of arguments as __init__
anna = WorkingStudent('Anna', 'MIT', 20.00, 'Student', 'US')
print(anna.name)
print(anna.school)
print(anna.salary)
print(anna.job_title)

# friend(cls) method can handle new additional methods required my
# WorkingStudent class __init__ with the *args placeholder
friend = WorkingStudent.friend(anna, 'Greg', 17.50, 'Engineer', location='US')
print(friend.name)
print(friend.school)
print(friend.salary)
print(friend.job_title)

# Therefore *args and **kwargs allow us to simplify things alot more when
# we don't know what's coming
