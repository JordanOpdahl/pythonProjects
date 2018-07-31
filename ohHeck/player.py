class Player:
    
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.__hand = []

    def addCard(self,card):
        self.__hand.append(card)
    
    def sortHand(self):
        self.__hand = sorted(self.__hand)
    
    def returnHand(self):
        return self.__hand

    def addScore(self,points):
        self.score = self.score + 10 + points
    
    def viewScore(self):
        return self.score
    
    def clearHand(self):
        self.__hand = []