x = [[700, 5, 12], [120, 18, 3900], ['tom', ['Tammy', 'susan', 'Martha'], 'Sam']]
# change 12 to 17
x[0][2]
# cap susans names
x[2][1][1] = Susan
print(x[2][1][1])

# list(indexed) dict(key,value pairs)
instructors = [
    {'first_name':  'cody', 'last_name': 'Thaller', 'email': 'c@gmail'},
    {'first_name': 'Tyler', 'last_name': 'Thaller', 'email': 't@gmail'},
    {'first_name': 'Shawn', 'last_name': 'Converse', 'email': 's@gmail'}
]

# change tylers last name to TBO
# this targets the last name in the 2nd spot
instructors[1]['last_name'] = "TBO"


stacks = {
    'Python': ["Gregory", 'Daniel', 'Collins,' 'Ashley'],
    'Mern': ['Schmidt', 'Fred', 'Lawson'],
    'C#': ['Stanley', 'Zack', 'Carl'],
    'Java': ['Harlan', 'Billie', 'Frank']
}

# stacks['Python'][1] = "Tim" #changes Daniel to Tim

# for key in stacks:
print(f"our key is {stacks['C#'][1]}")
