# UPDATING DICTIONARIES
import random
fruit = {
    'apple': 'sweet',
    'grapefruit': 'bitter',
    'lemon': 'sour'
}

fruit['grapes'] = 'juicy'

# IDEAL FOR ADDING A BUCNH OF KEYS
fruit.update({'watermelon': 'sweet', 'kiwi': 'tart'})

fruit.update(strawberry='sweet')

print(fruit)

# ITERATE THROUGH A DICTIONARY
bands = {
    'Metallica': 'Metal',
    'Thin Lizzy': 'Classic Rock',
    'Jim Croce': 'Folk',
    'Genisis': 'Prog'
}

for k in bands:
    print(k)  # prints the all keys

for k, elem in bands.items():
    print(k, elem)  # this will give me key, #value pairs

if 'Metallica' in bands:  # Used to find something in the dictionary
    print(bands['Metallica'])

# FINDING A VALUE IN A STRING AND LOGGING ITS VALUE
conjuctions = {"for": 0, "and": 0, "nor": 0, "but": 0, "or": 0, "so": 0
               }

origional_poem = "I still hear your voice when you sleep next to me I still feel your touch in my dreams Forgive me my weakness, but I dont know why Without you its hard to survive Cause every time we touch, I get this feeling And every time we kiss I swear I could fly Cant you feel my heart beat fast, I want this to last Need you by my side"

data = origional_poem.split()  # splits our string into individual items


for word in data:  # a value we're looking for in data
    if word in conjuctions:  # if that value is in conjunctions
        conjuctions[word] = + 1  # that word at counjuctions is increase by 1
print(conjuctions)


print(random.randint(2, 5))  # provides a random number between 2 and 5


# acessing items within the dictionary/list/dictionary
sweets = {
    'sweet_foods': [
        {'cake': 'chocolate', 'frosting': 'buttercream'},
        {'pie': 'apple', 'crust': "flaky"},
        {'ice cream': 'vanilla', 'mixins': 'gummy bears'}
    ]
}

print(sweets['sweet_foods'][0]['frosting'])  #

sweet_copy = sweets.copy()

