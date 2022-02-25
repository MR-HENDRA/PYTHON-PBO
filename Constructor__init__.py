class Hero: # template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        

hero1 = Hero("Alok",100,50,30)
hero2 = Hero("Hayato",95,45,40)
hero3 = Hero("Bima",90,60,35)
        
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)



