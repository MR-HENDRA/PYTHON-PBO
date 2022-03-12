class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print("{} dengan health: {}".format(self.name,self.health))

class Hero_intelligent(Hero):
    def __init__(self,name):
        #Hero.__init__(self, name, 500)
        super().__init__(name,500)
        super().showInfo()
        
class Hero_strenght(Hero):
    def __init__(self,name):
        #Hero.__init__(self, name, 450)
        super().__init__(name,450)
        super().showInfo()
        
hendra = Hero_intelligent('Hendra')
usman = Hero_strenght('Usman')







