# variables 
# we can store data in variables
# we can use variables to store different types of data such as numbers, strings, lists, dictionaries, etc.
# we can use variables to perform operations on the data they store
# we can use variables to make our code more readable and maintainable
# variable names should be descriptive and meaningful
# variable names should not start with a number or contain spaces
# variable names should not be the same as reserved keywords in Python
# example of variables
# Examples  of variables
name = "John"
age = 30
is_student = True
height = 1.75
# we can print the value of a variable
print(name)
print(age)
print(is_student)
print(height)


# we can perform operations on variables
# we can concatenate strings
full_name = name + " Doe"
print(full_name)


# we can perform arithmetic operations on numbers
age_next_year = age + 1
print(age_next_year)


# we can use variables in conditional statements
if is_student:
    print(name + " is a student.")
else:    print(name + " is not a student.") 

# we can use variables in loops
for i in range(5):
    print(i)       


# we can use variables in functions
def greet(name):
    return "Hello, " + name + "!"
greeting = greet(name)
print(greeting)


# we can change the value of a variable
name = "Jane"
print(name)     
# we can use variables to store user input
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

# we can use variables to store the result of a calculation
num1 = 10
num2 = 5
result = num1 + num2
print("The result of the addition is: " + str(result))

# we can use variables to store the state of a program
is_running = True
while is_running:
    user_input = input("Enter 'stop' to end the program: ")
    if user_input == "stop":
        is_running = False
print("Program has ended.") 

# we can use variables to store data in lists and dictionaries
fruits = ["apple", "banana", "cherry"]
print(fruits)
person = {"name": "John", "age": 30, "is_student": True}
print(person) 

# we can use variables to store data in tuples and sets
coordinates = (10, 20)
print(coordinates)
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers) 

# we can use variables to store data in classes and objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("John", 30)
print(person1.name)
print(person1.age)

# we can use variables to store data in modules and packages
import math         
pi_value = math.pi
print(pi_value) 



# working on lists
# is a collection of items that are ordered and changeable
# we can store different types of data in a list
# we can use lists to perform various operations such as adding, removing, and accessing items

# creating a list
# we can create a list using square brackets []
fruits = ["apple", "banana", "cherry"]
print(fruits)


# we can create an empty list and add items later
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)

# we can access items in a list using their index
print(fruits[0])
print(fruits[1]) 
print(fruits[2])  

# we can change the value of an item in a list
fruits[1] = "blueberry"
print(fruits)

# we can add items to a list using the append() method
fruits.append("orange")
print(fruits)

# we can remove items from a list using the remove() method
fruits.remove("apple")
print(fruits)

# we can use the extend() method to add multiple items to a list
fruits.extend(["grape", "melon"])
print(fruits)
# we can use the append() method to add a list as an item to another list
fruits.append(["kiwi", "pear"])
print(fruits)

# we can use the insert() method to add an item at a specific index in a list
fruits.insert(1,"strawberry")
print(fruits)

# we can use the pop() method to remove an item from a list and return its value
fruits.pop(2)
print(fruits)

fruits.remove("melon")
print(fruits)

# we can use the clear() method to remove all items from a list
fruits.clear()
print(fruits)
# we can use the len() function to get the number of items in a list
print(len(fruits))

items=[1, 2, 3, 4, 5]
print(len(items))

# we can use the sort() method to sort the items in a list
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print(numbers)

# we can use the reverse() method to reverse the order of items in a list
numbers.reverse()
print(numbers)

# we can use the index() method to get the index of the first occurrence of an item in a list
# print(fruits.index("grape"))   

# we can use the count() method to get the number of occurrences of an item in a list
print(fruits.count("strawberry"))

# we can use the copy() method to create a copy of a list
fruits_copy = fruits.copy()
print(fruits_copy)

# we can use the list() function to create a list from an iterable
string = "hello"
string_list = list(string)
print(string_list)

# we can use the split() method to split a string into a list of substrings
sentence = "This is a sentence."
words = sentence.split()
print(words)

# we can use the join() method to join a list of strings into a single string
joined_sentence = " ".join(words)
print(joined_sentence)   

# we can use list comprehension to create a new list based on an existing list
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)    

# we can use the filter() function to create a new list based on a condition
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# we can use the map() function to apply a function to each item in a list and create a new list
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# we can use the reduce() function from the functools module to apply a function cumulatively to the items in a list and reduce it to a single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

# we can use the enumerate() function to get the index and value of each item in a list
for index, value in enumerate(fruits):
    print(index, value) 

# we can use the zip() function to combine two or more lists into a single list of tuples
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = list(zip(list1, list2))
print(zipped)

# we can use the unzip() function to separate a list of tuples into individual lists
unzipped = list(zip(*zipped))
print(unzipped) 
