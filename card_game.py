# import dependencies
import algo

# card object storing face value from 1-10 and suit
class Card:
    def __init__(self,suit,face):
        self.suit = suit
        self.face = face

# deck object storing all card possibilites
class Deck:
    # make deck based on given suits and faces
    def __init__(self):
        # card value possibilities
        self.suits = ["red","black","yellow"]
        self.faces = [x for x in range(1, 11)]
        self.cards = []

        # make deck
        for suit in self.suits:
            for face in self.faces:
                self.cards.append(Card(suit,face))

        algo.shuffle(self.cards)

# player object to store cards in hand and player name
class Player:
    # name of player and cards held (local deck)
    def __init__(self,name):
        self.name = name
        self.deck = []
    
    # move i cards from origin to object deck
    def take_card(self,origin,i=1):
        algo.move(origin,self.deck,i)

# return winner based on each player's card
def round_winner(card1,card2):
    if card1.suit == card2.suit:
        return "p1" if card1.face > card2.face else "p2"
    else:
        ''' determine winner based on table below if suits unequal:
        CARD     CARD     WINNER
        Red      Black    Red
        Yellow   Red      Yellow
        Black    Yellow   Black
        '''
        for i in range(2):
            if card1.suit == "red" and card2.suit == "black":
                return "p1" if i == 0 else "p2"
            if card1.suit == "yellow" and card2.suit == "red":
                return "p1" if i == 0 else "p2"
            if card1.suit == "black" and card2.suit == "yellow":
                return "p1" if i == 0 else "p2"
            # reverse order of cards to find winner if not already found
            card1,card2 = card2,card1

# return winner of game based on number of cards
def game_winner(deck1,deck2):
    return "p1" if len(deck1) > len(deck2) else "p2"

# run full sequence
def play(name1,name2):
    # setup player objects
    players = [Player(name1),Player(name2)]

    # make & shuffle deck
    stack = Deck()
    deck = stack.cards

    # play rounds until deck exhausted
    while True:
        # take cards from top of deck
        for player in players:
            player.take_card(deck)

        # winner takes loser's cards
        if round_winner(players[0].deck[0],players[1].deck[0]) == "p1":
            players[0].take_card(players[1].deck)
        else:
            players[1].take_card(players[0].deck)
        
        # if deck is exhausted
        if len(deck) == 0:
            break

    # return winner and loser information
    return [players[0].name,players[0].deck,players[1].name,len(players[1].deck)] if game_winner(players[0].deck,players[1].deck) == "p1" else [players[1].name,players[1].deck,players[0].name,len(players[0].deck)] # winner name, winner's number of cards, loser name, loser's number of cards