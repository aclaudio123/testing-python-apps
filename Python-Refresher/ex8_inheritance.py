# inheritance and the importance of @classmethod
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        # returns the average of Students grades
        return sum(self.grades) / len(self.grades)

#   def friend(self, friend_name):
#       pass
#       # return a new Student called 'friend_name' in the same school as self.
#        return Student(friend_name, self.school)

    @classmethod  # converts a function to a class method
    # use keyword origin to indicate object where value will come from
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)  # friend object


anna = Student("Anna", "MIT")
# create a friend object using the method friend(self, friend_name), line14-16
# friend = anna.friend("Greg")
# print(friend.name)  # 'Greg'
# print(friend.school)  # 'MIT'


# ================= inheritance ==============================
# when a class defines it's own, and also inherit everything from another class
# we do this by passing the other class name as argument to the new class
class WorkingStudent(Student):  # Student is now a super class
    # our WorkingStudent (subclass) can also have it's own __init__ method
    def __init__(self, name, school, salary):
        # since subclass init has super class arguments in it, we can call them
        super().__init__(name, school)  # keyword super() to call Student class
        self.salary = salary  # salary is only argument not in super()


# create a WorkingStudent object, anna
anna = WorkingStudent(name='Anna', school='MIT', salary=20.00)
print(anna.salary)  # 20.00

# however,
# print(friend.salary)  # fails:  bcos friend was initialized using
# friend = anna.friend('Greg'); from line 25. anna is a Student object with
# no attribute salary defined in class Student.

# to call friend.salary, using anna as WorkingStudent object, we need to make a
# a friend object of WorkingStudent anna using the WorkingStudent class.
# We can do this by transforming our friend(self) function in Student class
# into a method using @classmethod which will use the keyword cls instead of
# self. This means that anytime we call @classmethod friend(cls), the output
# returned will be initialized by the class where the method was called. Hence
# reason for using cls.

# create a friend object using a WorkingStudent. anna = WorkingStudent() line42
# This means friend = anna.friend(name, school, salary). Since WorkingStudent
# __init__ takes 3 argument, friend(cls) should as well. So output returned by
# calling the friend(cls) method will be initialized by WorkingStudent class.
# WorkingStudent is inhering a method from Student class (inheritance)

# But anna's friend goes to the same school, 'MIT'. This means we can avoid
# passing a school value when creating the friend object. To do this, we add a
# a new keyword origin to our @classmethod signature to indicated where a value
# will come from. friend(cls, orign, friend_name, salary). We can use origin to
# return any additional values that anna's friend should have.
# Example: return cls(friend_name, origin.school, salary)

# this how we create the friend object to get values from origin
friend = WorkingStudent.friend(anna, 'Greg', 17.50)
print(friend.name)  # 'Greg'
print(friend.school)  # orign.school (anna.school) 'MIT' - anna object's school
print(friend.salary)  #
