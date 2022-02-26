class Hero: # template
    # class variable
    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
    # void function, metfod tanpa return, tanpa return
    def siapa(self):
        print("namaku adalah " + self.name)
        
    # method dengan argumen, tanpa return 
    def healthUp(self,up):
        self.health += up
        
    # method dengan return 
    def getHealt(self):
        return self.health
        
hero1 = Hero("Alok",100,50,30)
hero2 = Hero("Hayato",95,45,40)
hero3 = Hero("Bima",90,60,35)

hero1.siapa()
hero1.healthUp(30)

# print(hero1.health)
print(hero1.getHealt())
