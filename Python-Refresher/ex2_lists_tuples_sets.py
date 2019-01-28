# List
# - Uses []
# - Mutable (size of the list can be increased) i.e. more items can be added
# Ordered i.e. items print out in same order inside the []
list_grades = [77, 80, 90, 95, 100]
list_grades.append(105)  # append() used for adding items at end
print(sum(grades) / len(grades))

# list operations
print(list_grades[0])  # prints item at position (index) 0
list_grades[0] = 60   # replaces item in index 0 with 60
dir(list)  # prints out all operations that can be performed on list


# ======================= Tuples ========================================
# - Uses ()
# - Immutable ( size can't be increased) i.e. you can't added more items to it
tuple_grades = (77, 80, 90, 95, 100)  # Immutable
print(list_grades[0])  # prints item at index 0
tuple_grades[0] = 60  # TypeError: tuple does not support item assignment

# tuple operations
dir(tuple)  # prints tuple attributes.
tuple_grades.count(80)  # prints how many times 80 appears in tuple_grades
tuple_grades.index(100)  # prints the index of 100


# ======================= Sets ========================================
# Sets
# - Uses {}
# - Collection of unique items
# - Unordered i.e. set items don't have any order.
# - Mutable (size of the set can be increased)
# A Set is a collection of unique and Unordered elements
set_grades = {77, 80, 90, 95, 100, 100}
print(set_grades)  # items will be print in any order and only unique items
set_grades.add(60)  # adds 60 into the set. Sets are Mutable

# Set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# find intersection -- will print set([1,3,5])
# that is all unique numbers in both sets.
print(your_lottery_numbers.intersection(winning_numbers))

# find the union -- will print set([1, 2, 3, 4, 5, 7, 9, 11])
# that is a union of only unique elements
print(your_lottery_numbers.union(winning_numbers))

# find difference -- prints {3, 4}
print({1, 2, 3, 4}.difference({1, 2}))


# ============== Exercise ========================
# Create a list, called my_list, with three numbers. The total of the numbers
# added together should be 100.


# Create a tuple, called my_tuple, with a single value in it


# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}
