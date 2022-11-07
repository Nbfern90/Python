# 1
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [{'x': 10, 'y': 20}]


# 1 x[1][0] =15
# 2 students[0]['last_name'] = 'Bryant'
# 3 sports_directory['scoccer'][0] = 'Andres'
# 4 z[0]['y'] = 30


# 2
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


3


def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4
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
