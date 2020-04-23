import card_game,leaderboard

# run game
results = card_game.play(input("Please enter the name of player 1: "),input("Please enter the name of player 2: "))
print(results[0],"won with",len(results[1]),"cards against",str(results[2])+"\'s",results[3]) # winner name, winner's number of cards, loser name, loser's number of cards

# print cards that winner had
print(results[0],"had:")
for i in range(len(results[1])):
    print(results[1][i][0].capitalize(),results[1][i][1]) # suit, value

# update leaderboard and store top 5
leaderboard.add(results[0],len(results[1]))
top_5 = leaderboard.top_5()

for i in range(len(top_5)):
    print(str(i+1)+".",top_5[i][0],top_5[i][1]) # leaderboard pos, name, score