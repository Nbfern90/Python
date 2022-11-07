people = [
    {'first_name': 'John', 'last_name': 'Smith', 'favorite_food': 'Pizza'},
    {'first_name': 'Dave', 'last_name': 'Davidson', 'favorite_food': 'Tacos'},
    {'first_name': 'Matt', 'last_name': 'Leavey', 'favorite_food': 'Hot Dogs'},
    {'first_name': 'Ruben', 'last_name': 'Sanders', 'favorite_food': 'Hamburger'},
    {'first_name': 'Larry', 'last_name': 'Fine', 'favorite_food': 'Hamburger'}
]

people[1]['favorite_food'] = 'cake'  # updates favorite food

print(people)

# dictionary
fav_sport = {
    'bob': 'football',
    'jim': 'golf',
    'larry': 'tennis',
    'mike': 'hockey,',
    'dave': 'bowling'
}
fav_sport['mike'] = 'racing'  # updates a value
fav_sport['roy'] = 'swimming'  # adds new key value pair to dict
print(fav_sport.key())  # prints all keys
print(fav_sport.values())  # prints all values
print(fav_sport.items())  # prints all key,value pairs


# accesses the fist and last names
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for i in some_list:
        print("first_name - " + i['first_name'] +
              ", last_name - " + i['last_name'])


iterateDictionary(students)

# prints all the first names followed by the last names
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for i, val in some_dict.items():
        print(len(val), i.upper())
        for j in val:
            print(j)


printInfo(dojo)

