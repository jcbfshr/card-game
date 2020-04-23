# import dependencies
import algo

# initialise global deck and card value possibilities
suits = ["red","black","yellow"]
faces = [x for x in range(1, 11)]
deck = []

# player object to store cards in hand and player name
class Player:
    def __init__(self,name):
        self.name = name
        self.deck = []
    
    # move i cards from origin to object deck
    def take_card(self,origin,i=1):
        algo.move(origin,self.deck,i)

# create deck of cards and shuffle
def prepare():
    # make deck based on given suits and faces
    for suit in suits:
        for face in faces:
            deck.append([suit,face])

    algo.shuffle(deck)
    return deck

# return winner based on each player's card
def round_winner(card1,card2):
    if card1[0] == card2[0]: # if suits are equal
        return "p1" if card1[1] > card2[1] else "p2"
    else:
        ''' determine winner based on table if suits unequal:
        CARD     CARD     WINNER
        Red      Black    Red
        Yellow   Red      Yellow
        Black    Yellow   Black
        '''
        for i in range(2):
            if card1[0] == "red" and card2[0] == "black":
                return "p1" if i == 0 else "p2"
            if card1[0] == "yellow" and card2[0] == "red":
                return "p1" if i == 0 else "p2"
            if card1[0] == "black" and card2[0] == "yellow":
                return "p1" if i == 0 else "p2"
            # reverse order of cards to find winner if not already found
            card1,card2 = card2,card1

# return winner of game based on number of cards
def game_winner(deck1,deck2):
    return "p1" if len(deck1) > len(deck2) else "p2"

# run full sequence
def play(name1,name2):
    # setup player objects
    p1 = Player(name1)
    p2 = Player(name2)

    # make & shuffle deck
    prepare()

    # play rounds until deck exhausted
    while True:
        # take cards from top of deck
        p1.take_card(deck)
        p2.take_card(deck)
        
        # winner takes loser's cards
        if round_winner(p1.deck[0],p2.deck[0]) == "p1":
            p1.take_card(p2.deck)
        else:
            p2.take_card(p1.deck)
        
        # if deck is exhausted
        if len(deck) == 0:
            break

    # return winner and loser information
    return [p1.name,p1.deck,p2.name,len(p2.deck)] if game_winner(p1.deck,p2.deck) == "p1" else [p2.name,p2.deck,p1.name,len(p1.deck)] # winner name, winner's number of cards, loser name, loser's number of cards