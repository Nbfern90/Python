import random
num1 = 42  # variable Declaration
x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")


class EmptyClass:
    pass


# pass is used for situations where we need a block statement but aren't sure what to put there yet
for val in my_string:
    pass

# DATA TYPES
#   PRIMITIVE DATA TYPES
# Booleans
is_hungry = True
has_freckles = False
# Numbers
age = 25  # storing as integer
weight = 160.57  # storin as a float
# Strings
name = "joe", "dave", "john",

#   COMPOSITE TYPES = Collections of the above primitie types
# Tuples-a type of data that is immutable(can't be motified)
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
# ERROR: cannot be modified ('tuple' object does not support item assignment)
dog[1] = 'dachshund'

# Lists-A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)  # output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)  # output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)  # output: ['Francis', 'Oliver']

# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# updates if the key exists, adds a key-value pair if it doesn't
new_person['name'] = 'Jack'
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')  # removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

# COMMON FUNCTIONS
# If we're ever unsure of a value or variable's data type, we can use the type function to find out. For example:

print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))  # output: 11

# RANDOM -Python does not have a built in random number generator, use the random module instead.

print(random.randint(2, 5))  # provides a random number between 2 and 5


# STRING INTERPOLATION-injecting variables into our strings

# F-strings -To construct a f-string, place an f right before the opening quotation

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

# string.format()-Prior to f-strings, string interpolation was accomplished with the .format()  To use it, type out the full string, replacing any words that will get their values from variables with {}. Then call the format method on the string, passing in arguments in the order in which they should fill the {} placeholders.

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# EVEN OLDER METHOD
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

# BUILT-IN STRING METHODS
x = "Hello world"
print(x.title())


# LOOPS

capitals = {"Washington": "Olympia", "California": "Sacramento", "Idaho": "Boise",
            "Illinois": "Springfield", "Texas": "Austin", "Oklahoma": "Oklahoma City", "Virginia": "Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc
