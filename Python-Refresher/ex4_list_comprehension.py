my_list = [0, 1, 2, 3, 4]

# list comprehension builds a list of elements
# building a list of x
an_equal_list = [x for x in range(5)]  # range(5) = [0, 1, 2, 3, 4]

multiply_list = [x * 3 for x in range(5)]

# building a list of even numbers
print([n for n in range(10) if n % 2 == 0])

people_you_know = ["Rolf", " John", "anna", "GREG"]

# build a list of people eliminating any whitespaces and lowercasing them
normalized_people = [person.strip().lower() for person in people_you_know]
print(normalized_people)
