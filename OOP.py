class Hero: # template
    pass


hero1 = Hero() # Object / instance (instansiate)
hero2 = Hero()
hero3 = Hero();

hero1.name = "Jota"
hero1.health = 100

hero2.name = "Alok"
hero2.health = 150

hero3.name = "Hayato"
hero3.health = 90

print(hero1)
print(hero1.__dict__)
print(hero1.name)

print(hero2)
print(hero2.__dict__)
print(hero2.name)

print(hero3)
print(hero3.__dict__)
print(hero3.name)