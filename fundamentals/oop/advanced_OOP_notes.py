class Wizard:
    pointy_hat = True
    robes = True

    def __init__(self, name, magic_school, spell_book, health=100, mana=100):
        self.name = name
        self.magic_school = magic_school
        self.spell_book = spell_book
        self.health = health
        self.mana = mana

    def cast(self, spell_name, target):
        if spell_name not in self.spell_book:
            print('Invalid spell, try again')
            return self

        mana_reduced = self.spell_book[spell_name]["mana_cost"]

        if mana_reduced > self.mana:
            print(
                f"As hard as {self.name} tries, they just can't muster up enough energy and the spell fails")
            return self
        self.mana -= mana_reduced

        # reduce target's health by spell's damage
        spell_damage = self.spell_book[spell_name]["damage"]
        target.health -= spell_damage

        # print a description of what happened
        # Example: Rincewind launches a fireball at Joe, dealing 25 damage at the cost of 30 mana
        print(
            f"{self.name} {self.spell_book[spell_name]['description']} {target.name}, dealing {spell_damage} damage at the cost of {mana_reduced} mana.")

        # what if the target dies?
        if target.health <= 0:
            # Joe dies a miserable death from Rincewind's Fireball
            print(
                f"{target.name} dies a miserable death from {self.name}'s {spell_name}")

        return self


class Character:
    def __init__(self, name, abilities, health=100, mana=100):
        self.name = name
        self.abilities = abilities
        self.health = health
        self.mana = mana

    def attack(self, ability, target):
        if ability not in self.abilities:
            print('Invalid ability, try again')
            return self

        mana_cost = self.abilities[ability]['mana_cost']

        if mana_cost > self.mana:
            print(f'{self.name} does not have enough mana.')
            return self

        damage_dealt = self.abilities[ability]['damage']

        print(
            f"{self.name} {self.abilities[ability]['description']} {target.name}, dealing {damage_dealt} damages at the cost of {mana_cost} mana")
        target.take_damage(damage_dealt)

    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            print(f'{self.name} Dies')
            return self


class Wizard(Character):
    pointy_hat = True
    robes = True

    def __init__(self, name, spell_book, magic_school, health=75, mana=150):
        super().__init__(name, spell_book, health, mana)
        self.magic_school = magic_school


rincewind_spells = {
    "Fireball": {
        "description": "Launches a fireball at enemy",
        "damage": 25,
        "mana_cost": 30
    }
}

rincewind = Wizard("Rincewine", rincewind_spells, "Failure", 50)

joe = Wizard("Joe", {}, "plummer", mana=0)

rincewind.attack("Fireball", joe)


class Ninja(Character):
    is_sneaky = True

    def __init__(self, name):
        abilities = {
            "Sneak": {
                "description": "sneaks up to and stabs",
                "damage": 40,
                "mana_cost": 70
            },
            "Smoke bomb": {
                "description": "throws down a smoke bomb, vanishing instantly",
                "damage": 0,
                "mana_cost": 25
            }
        }
        super().__init__(name, abilities, 70, 50)

    def meditate(self):
        print(f"{self.name} meditates, restoring 10 health.")

        self.health += 10

        return self
