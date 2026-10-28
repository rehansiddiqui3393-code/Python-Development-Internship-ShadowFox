# Section 8: Classes and Objects

class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return (f"Name: {self.name} | Age: {self.age} | Gender: {self.gender} | "
                f"Super Power: {self.super_power} | Weapon: {self.weapon}")

    def is_leader(self):
        if self.name == "Captain America":
            return f"{self.name} is the leader of the Avengers"
        return f"{self.name} is not the leader"


super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]

captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Shield")
iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir")
hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")

team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

for hero in team:
    print(hero.get_info())
    print(hero.is_leader())
    print()
