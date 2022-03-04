from traceback import print_tb


class Hero:
    
    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
        
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def attackPower(self):
        return self.__attackPower
    
    # setter
    def diserang(self,serangPower):
        self.__health -= serangPower
        
    def power(self,nilaibaru):
        self.__attackPower += nilaibaru
        
# awal dari game
Endangk = Hero("Endangk",100,50)

# game berjalan

print(Endangk.getName())
print(Endangk.getHealth())
Endangk.diserang(10)
print(Endangk.getHealth())
print(Endangk.attackPower())
Endangk.power(25)
print(Endangk.attackPower())