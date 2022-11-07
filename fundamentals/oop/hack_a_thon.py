
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
        # potential edge case: what if that's not a spell?
        if spell_name not in self.spell_book:
            print("Invalid spell, try again!")
            return self
        # reduce wizard mana by spell's cost
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

    def __repr__(self):
        return f"{self.name}, wizard of {self.magic_school}.\nCurrent stats: \nHealth: {self.health}\nMana: {self.mana}"


rincewind_spells = {
    "Fireball": {
        "description": "launches a fireball at",
        "damage": 35,
        "mana_cost": 30
    }
}
rincewind = Wizard("Rincewind", "Failure", rincewind_spells, 100, 200)
joe = Wizard("Joe", "Plumbing", {})

print(rincewind)
print(joe)
rincewind.cast("Fireball", joe)
print(rincewind)
print(joe)

rincewind.cast("Fireball", joe).cast("Fireball", joe).cast("Fireball", joe)

print(rincewind.pointy_hat)
