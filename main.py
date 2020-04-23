import cardGame

results = cardGame.play(input("Please enter the name of player 1: "),input("Please enter the name of player 2: "))
print(results[0],"won with",len(results[1]),"cards against",str(results[2])+"\'s",results[3])
print(results[0],"had:")
for i in range(len(results[1])):
    print(results[1][i][0].capitalize(),results[1][i][1])