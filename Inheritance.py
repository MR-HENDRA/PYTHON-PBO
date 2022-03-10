class Hero:
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

hendra = Hero("Hendra",100)
usman = Hero_intelligent("Usman",95)
ali = Hero_strength("ali",90)

print(hendra.name)
print(usman.name)
print(ali.name)