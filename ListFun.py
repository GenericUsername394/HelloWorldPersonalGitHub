import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3
list_ints = [100, 1, 10, 20]
# there are unique indexes for each element in the list
# 0-based... meaning the first element is at 0, and the last element is at n - 1
# where n is the number of elements in the list

print(list_ints[0])
print(list_ints[-4])

# types can be mixed in a list
list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)
print(type(list_numbers))
# lists are mutable (they can be changed)
list_numbers[0] = "hello"
print(list_numbers)

# use len() to find out how many elements are in a list
print(len(list_numbers))
list_numbers.append("another element")
# print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list
print(list_numbers[len(list_numbers) - 1])

# we can declare an empty list!
empty_list = []
print(len(empty_list))

# we can have lists of lists (2D or ND)
nested_list = [[0, 1], [2], [3], [4, 5], []]
print(len(nested_list))
print(len(nested_list[0]))

# looping through list items
candies = ["twix", "reeses", "oreos", "snickers"]
print(candies)

for candy in candies:
    print(candy)

i = 0
while i < len(candies):
    print(i, candies[i])
    i += 1

i = 0
for i in range(len(candies)):
    print(i, candies[i])

# common list operators
# list concatenation... adding 2 lists together
print(candies)
candies += ["m&ms", "starburst"]
print(candies)
# list repetition... repeating elements in a list
bag_o_candies = 5 * ["twix", "snickers"]
print(bag_o_candies)
# list slicing
print(candies[1:3]) # : is the slice operator. start index is inclusive
# end index is exclusive
# if you ever need a copy of a list, you can simply use the : with no start or end indices
copy_of_candies = candies[:]
copy_of_candies[0] = "TWIX"
print(copy_of_candies)
print(candies)

# list methods 
candies.remove("reeses")
print(candies)

# 1D PRACTICE PROBLEM 
# In ListFun, write code that generates 20 random numbers between 1 and 10 inclusive 
# and puts them in a 1D list. 
random.seed(0)
numbers = []
for i in range(20):
    rand_num = random.randrange(1, 11) # [1, 11) -> [1, 10]
    numbers.append(rand_num) # append adds an element to the end of list
print(numbers)

# The program then does the following using the list:
# 1. Prints the numbers all one line, each number separated by a space
def pretty_print(numbers):
    for num in numbers:
        print(num, end=" ")
    print()
pretty_print(numbers)
# 2. Sorts the list using a list method
# numbers.sort() # inplace sort (modifies the list)
# pretty_print(numbers)
# use the built-in sorted function (doesn't modify the list
# produces a new list)
sorted_numbers = sorted(numbers)
pretty_print(sorted_numbers)
pretty_print(numbers)

# 3. Prints the largest and smallest number in the list
print("min:", min(numbers), "max:", max(numbers))
# Hint: can you take advantage of the current ordering of your list?
print("min:", sorted_numbers[0], "max:", sorted_numbers[-1])

# 4. Determines the number of times a user-specified number is in the list
# user_num = int(input("Enter a number in [1, 10]: "))
# count = 0
# for num in numbers:
#     if num == user_num:
#         count += 1
# print("there are", count, "of", user_num, "in the list")
# # 5. Removes all instances of a user-specified number in the list. 
# # If the number is not in the list print the message: "Sorry, your number is not here!"
# # Note: for practice with functions, try solving this problem using functions :)
# user_num = int(input("Enter a number in [1, 10] to remove: "))
# if user_num not in numbers:
#     print("Sorry, your number is not here!")
# else: #user_num in numbers
#     while user_num in numbers:
#         numbers.remove(user_num)

# print(sorted(numbers))

# # warm up
# Define and call a function that accepts two lists
# The function returns two Boolean values:
# The first value is true if the two lists have the same first item.
# The second value is true if the two lists have the same last item.
# Check to make sure both lists have at least one item first (return falses on this case).
# Display the returned results.
# Test your function with a few different hard-coded lists.
def has_same_first_and_last_element(list1, list2):
    same_first = False 
    same_last = False 
    if len(list1) > 0 and len(list2) > 0: # ensure at least one item in each
        if list1[0] == list2[0]:
            same_first = True 
        if list1[-1] == list2[-1]:
            same_last = True 

    return same_first, same_last 

print(has_same_first_and_last_element([], []))
print(has_same_first_and_last_element([1, 2], [1, 2]))
print(has_same_first_and_last_element([0, 2], [1, 2]))
print(has_same_first_and_last_element([1], [1]))

# (more on) LIST METHODS
# append()
holidays = ["valentines"]
holidays.append("chinese new year")
print(holidays)
# extend()
holidays.extend(["groundhog day", "christmas"])
print(holidays)
# += (plus-assign) (list concatenation) does the same thing extend
holidays += ["international womens days", "april fools day"]
print(holidays)
# pop() is like remove(), except you pass in an index for an item to remove
groundhog = holidays.pop(2)
print(groundhog, holidays)

# create a string from a list of strings
valentines = ["v", "al", "e", "nti", "n", "e", "s"]
# string method join()
valentines_str = "*".join(valentines)
print(valentines_str)
# string back to a list
# list()
valentines_list = list(valentines_str)
print(valentines_list)
# CSV parser (next class)
# comma separated value
christmas = "c,h,r,i,s,t,m,a,s"
# string method split()
pieces_list = christmas.split(",")
print(pieces_list)
pieces_list = valentines_str.split("*")
print(pieces_list)

# 2D LIST PRACTICE PROBLEMS
# In ListFun, write code that generates 50 random numbers 
# between 1 and 10 inclusive and puts them in a 2D list 
# that is 10x5 (e.g. 10 rows and 5 columns). The program 
# then does the following using the list:
# 2D list is a nested list
# or in other words it is 1D where each element is a list
table = []
for _ in range(10):
    row = []
    for _ in range(5):
        rand_num = random.randint(1, 10)
        row.append(rand_num)
    table.append(row)
print(table)

# 1. Prints the numbers in a nice grid format (like a table)
for row in table:
    for value in row:
        print(value, end="\t")
    print()

# 2. Prints the largest and smallest number in the list
# 3. Determines the number of times a user-specified number 
# is in the list
# 4. Removes all instances of a user-specified number in the list.
# If the number is not in the list print the message: 
# "Sorry, your number is not here!"
# Note: for practice with functions, try solving this 
# problem using functions :)