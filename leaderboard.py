# open leaderboard file
def access():
    try:
        file = open("leaderboard.txt","r")
    except:
        file = open("leaderboard.txt","w+")
    leaderboard = [] # start with empty leaderboard

    # run through each entry in leaderboard and append to array
    for line in file:
        leaderboard.append([int(char) if char.isdigit() else char for char in line.strip().split(',')]) # if int -> convert to int, append [name,score]
    
    file.close()
    return leaderboard

# update leaderboard file
def update(new_leaderboard):
    file = open("leaderboard.txt","w")

    for entry in new_leaderboard:
        file.write(str(entry[0])) # name
        file.write(",")
        file.write(str(entry[1])) # score
        file.write("\n")

    file.close()

# add player to leaderboard file
def add(name,score):
    leaderboard = access()

    # sort leaderboard with new entry
    leaderboard.append([name,score])
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)

    # only store top 5
    update(leaderboard[:5]) 

# return top 5 on leaderboard
def top_5():
    leaderboard = access()
    return leaderboard[:5]