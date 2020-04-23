import random

# Fisher–Yates shuffle Algorithm
def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randrange(0,i+1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

# move i cards from top of y to the top of x
def move(y,x,i=1):
    for i in range(i):
        x.insert(0,y[0])
        y.remove(y[0])
    return y,x