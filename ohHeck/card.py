class Card:
    def __init__(self,value,suit):
        self.__value = value
        self.__suit = suit
    
    def getValue(self):
        return self.__value
    
    def getSuit(self):
        return self.__suit
        