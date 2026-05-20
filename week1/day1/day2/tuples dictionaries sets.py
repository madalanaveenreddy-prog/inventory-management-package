# tuples
# A tuple is an ordered, immutable collection of items. Tuples are defined using parentheses () and can contain any type of data. Once a tuple is created, 
# its contents cannot be changed.
# creating a tuple
coordinates = (10, 20)
print(coordinates)  

# we can access items in a tuple using their index
print(coordinates[0])
print(coordinates[1])   
# we cannot change the value of an item in a tuple
# coordinates[0] = 30  # This will raise a TypeError    
# we can use tuples to store related data that should not be changed, such as coordinates or RGB color values 

# tuples can also be used as keys in dictionaries, while lists cannot because they are mutable
 # tuple methods
# count() method returns the number of times a specified value appears in the tuple
my_tuple = (1, 2, 3, 4, 2, 5)
print(my_tuple.count(2))  
# index() method returns the index of the first occurrence of a specified value in the tuple
print(my_tuple.index(3))        


# we can also use tuples to unpack values into variables
point = (10, 20)
x, y = point
print(x)
print(y)   

# we can use the zip() function to combine two or more tuples into a single tuple of tuples
let1=(1,2,3)
let2=(4,5,6)
some=zip(let1,let2)
print(list(some))

# sets
# A set is an unordered collection of unique items. Sets are defined using curly braces {} and can contain any type of data. Sets do not allow duplicate values and do not maintain the order of items.
# creating a set
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)       
# we can add items to a set using the add() method
unique_numbers.add(6)
print(unique_numbers)
# we can remove items from a set using the remove() method
unique_numbers.remove(3)
print(unique_numbers)
# we can check if an item is in a set using the in keyword
print(4 in unique_numbers)
print(3 in unique_numbers)
# we can use sets to store unique items and perform set operations such as union, intersection, and difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# union of sets
union_set = set1.union(set2)
print(union_set)
# intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)
# difference of sets            
difference_set = set1.difference(set2)
print(difference_set)   
# we can also use sets to remove duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
unique_list = list(unique_set)
print(unique_list)  
# we can also use sets to check for common items between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1 = set(list1)
set2 = set(list2)
common_items = set1.intersection(set2)
print(common_items)
# we can also use sets to check for unique items in a list
list3 = [1, 2, 3, 4, 4, 5]
unique_items = set(list3)
print(unique_items) 

# dictionaries
# A dictionary is an unordered collection of key-value pairs. Dictionaries are defined using curly braces {} and consist of keys and values. Keys must be unique and immutable, while values can be of any type and can be duplicated.
# creating a dictionary
person = {"name": "John", "age": 30, "is_student": True}
print(person)
# we can access values in a dictionary using their keys
print(person["name"])
print(person["age"])
print(person["is_student"])
# we can change the value of an item in a dictionary
person["age"] = 31
print(person)
# we can add new key-value pairs to a dictionary
person["city"] = "New York"
print(person)
# we can remove key-value pairs from a dictionary using the del keyword
del person["is_student"]
print(person)
# we can check if a key is in a dictionary using the in keyword
print("name" in person)
print("is_student" in person)
# we can use dictionaries to store related data that can be accessed using keys, such as a person's name, age, and city of residence    
# we can also use dictionaries to store data in a structured way, such as a list of dictionaries to represent a collection of items with their attributes
people = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 35}
]
print(people)           
# we can also use dictionaries to count the frequency of items in a list
my_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
frequency = {}
for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)    
# we can also use dictionaries to group items by a common attribute
people = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 30}
]
age_groups = {}
for person in people:
    age = person["age"]
    if age in age_groups:
        age_groups[age].append(person["name"])
    else:
        age_groups[age] = [person["name"]]
print(age_groups)   
# we can also use dictionaries to store data in a nested structure, such as a dictionary of dictionaries to represent a collection of items with their attributes and sub-attributes
people = {
    "John": {"age": 30, "city": "New York"},
    "Jane": {"age": 25, "city": "Los Angeles"},
    "Doe": {"age": 35, "city": "Chicago"}
}
print(people)       
# we can access nested values in a dictionary using multiple keys
print(people["John"]["age"])
print(people["Jane"]["city"])       
# we can also use dictionaries to store data in a way that allows for easy retrieval and manipulation, such as using a dictionary to represent a phone book where the keys are names and the values are phone numbers
phone_book = {
    "John": "123-456-7890",
    "Jane": "987-654-3210",
    "Doe": "555-555-5555"
}
print(phone_book)       
# we can access phone numbers using names as keys
print(phone_book["John"])
print(phone_book["Jane"])   
# we can also use dictionaries to store data in a way that allows for easy updating and maintenance, such as using a dictionary to represent a product inventory where the keys are product names and the values are quantities
inventory = {
    "apple": 10,
    "banana": 20,
    "cherry": 15            
}
print(inventory)
# we can update inventory quantities using product names as keys
inventory["apple"] += 5
inventory["banana"] -= 10
print(inventory)            
# we can also use dictionaries to store data in a way that allows for easy searching and filtering, such as using a dictionary to represent a collection of books where the keys are book titles and the values are dictionaries containing book attributes such as author and genre
books = {
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "genre": "Fiction"},
    "To Kill a Mockingbird": {"author": "Harper Lee", "genre": "Fiction"},
    "A Brief History of Time": {"author": "Stephen Hawking", "genre": "Science"}
}
print(books)
# we can search for books by genre using a loop and conditional statements
for title, attributes in books.items():
    if attributes["genre"] == "Fiction":
        print(title)            
# we can also use dictionaries to store data in a way that allows for easy aggregation and analysis, such as using a dictionary to represent a collection of sales data where the keys are product names and the values are lists of sales amounts
sales_data = {
    "apple": [100, 150, 200],
    "banana": [50, 75, 125],
    "cherry": [200, 250, 300]       
}
print(sales_data)
# we can calculate total sales for each product using a loop and the sum() function
total_sales = {}
for product, sales in sales_data.items():
    total_sales[product] = sum(sales)
print(total_sales)  
# we can also use dictionaries to store data in a way that allows for easy visualization and reporting, such as using a dictionary to represent a collection of survey responses where the keys are question prompts and the values are lists of responses
survey_responses = {
    "What is your favorite color?": ["red", "blue", "green", "red", "blue"],
    "What is your favorite food?": ["pizza", "sushi", "burger", "pizza", "sushi"]
}
print(survey_responses)
# we can visualize survey responses using a loop and the Counter class from the collections module