# import dependencies
import algo,unittest

# initialise variables
suits = ["red","black","yellow"]
faces = [x for x in range(1, 11)]
deck = []

# player object to store cards in hand and player name
class Player:
    def __init__(self,name):
        self.name = name
        self.deck = []
    
    def take_card(self,origin):
        algo.move(origin,self.deck)

# create deck of cards and shuffle
def prepare():
    for i in range(len(suits)):
        for x in range(len(faces)):
            deck.append([suits[i],faces[x]])
    algo.shuffle(deck)
    return deck

def round_winner(card1,card2):
    if card1[0] == card2[0]:
        return "p1" if card1[1] > card2[1] else "p2"
    else:
        for i in range(2):
            if card1[0] == "red" and card2[0] == "black":
                return "p1" if i == 0 else "p2"
            if card1[0] == "yellow" and card2[0] == "red":
                return "p1" if i == 0 else "p2"
            if card1[0] == "black" and card2[0] == "yellow":
                return "p1" if i == 0 else "p2"
            # reverse order of cards to find winner if not already found
            card1,card2 = card2,card1

def game_winner(deck1,deck2):
    return "p1" if len(deck1) > len(deck2) else "p2"

def play(name1,name2):
    p1 = Player(name1)
    p2 = Player(name2)
    prepare()
    while True:
        p1.take_card(deck)
        p2.take_card(deck)
        if round_winner(p1.deck[0],p2.deck[0]) == "p1":
            p1.take_card(p2.deck)
        else:
            p2.take_card(p1.deck)
        if len(deck) == 0:
            break
    return [p1.name,p1.deck,p2.name,len(p2.deck)] if game_winner(p1.deck,p2.deck) == "p1" else [p2.name,p2.deck,p1.name,len(p1.deck)]