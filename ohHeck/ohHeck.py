from player import Player
from card import Card
import random


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
            print(player.name)
            for card in hand:
                print(card.getValue()," + ",card.getSuit())
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