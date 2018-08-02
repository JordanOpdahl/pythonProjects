from player import Player
from card import Card
import random
import pygame, sys


#Loading Images for cards
pygame.init()
#twoClub = pygame.image.load('images/2C.png')
display = pygame.display.set_mode((300,300))


#def pyGamePlay():
   # while True:
       # pygame.event.pump()
        #for event in pygame.event.get():
        #    if event.type == quit:
        #        pygame.quit()
        #        sys.exit()
        #pygame.draw.rect(display,(0,255,0),(100,50,20,20))
        #pygame.display.update()
        #playGame()


def playGame():
    #Initialize Game State
    global numOfPlayers
    numOfPlayers = (int(input("How many players are there? ")))
    playerList = []
    for i in range(1,numOfPlayers+1):
        nameOfPlayer = input("Name of player "+str(i)+":")
        playerList.append(Player(nameOfPlayer))

    currentDealer = 0
    global numOfRounds
    global currentCardCount
    global suits
    numOfRounds = 52//numOfPlayers
    currentCardCount = numOfRounds
    suits = ["spades","club","diamond","heart"]
 

    while(currentCardCount != 0):
        shuffleDeck(playerList,currentCardCount,currentDealer)
        currentDealer = (currentDealer + 1) % numOfPlayers
        currentCardCount -= 1
        for player in playerList:
            hand = player.returnHand()
            hand = sorted(hand,key=lambda card: (card.getSuit(),card.getValue()))
            print(player.name)
            for card in hand:
                print(card.getValue(),card.getSuit())
            print("")
            player.clearHand()
        print("-------------------------------------------------------------")

def shuffleDeck(listOfPlayers,numToDeal,currentDealer):
    deck = [Card(value,suit) for value in range(13) for suit in suits]
    random.shuffle(deck)

    currentCard = 0
    currentPlayer = currentDealer
    while(currentCard < currentCardCount * numOfPlayers):
        listOfPlayers[currentPlayer].addCard(deck[currentCard])
        currentCard += 1
        currentPlayer += 1
        currentPlayer %= numOfPlayers
    



if __name__ == '__main__':
    playGame()