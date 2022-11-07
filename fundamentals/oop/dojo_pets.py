class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5

    def noise(self):
        print("The Animals makes a curious noise.")


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self. treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print("Pet got exercise for today")
        return self

    def feed(self):
        self.pet.eat()
        print("Pet is no longer hungry")
        return self

    def bathe(self):
        self.pet.noise()
        print("Pet is no longer dirty")
        return self


sparky = Pet("Sparky", "Dog", "Uses and Flushes Toilet", 100, 100)

red_ninja = Ninja("John", "Smith", sparky, "Salami", "Pedigree")


red_ninja.feed().walk().bathe()
