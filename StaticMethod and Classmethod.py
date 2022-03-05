class Hero:
    
    # private class variable
    __jumlah = 0;
    
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
        
    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def GetJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def GetJumlah3(cls):
        return cls.__jumlah
    
sniper = Hero("sniper")
print(Hero.GetJumlah2())
rikimaru = Hero("rikimaru")
print(sniper.GetJumlah2())
drowranger = Hero("drowranger")
print(sniper.GetJumlah3())   
        