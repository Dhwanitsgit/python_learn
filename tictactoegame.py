


game = [
        [0, 0, 0],
        [0 ,0 ,0],
        [0, 0, 0]
        ]


def game_board(game_map, player_no=0, row=0, column=0, justDisplay=False):
    print("0 , 1 , 2")
    if not justDisplay:
        game_map[row]  [column] = player_no
    for count , row in enumerate(game_map):
        print(count,row)

    return game_map
game = game_board(game,justDisplay=True)
game=game_board(game,player_no=1,row=1,column=1) 





def winner(current_game=1):
    for row in game:
        print(row)
    if row.count(row[0]) == len(row) and row[0]!=0:
        print("winner")
   
        

print(len(game))
#cols = list
#rows = range(len(game))
diags = []
for col , row in enumerate(reversed(range(len(game)))):
    print(col,row)
#print(len(game))
    diags.append(game[row][col])
diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])



"""


x = 1
def test():
    x = 2
test()
print(x)



x = 1
def test():
    global x
    x = 2
test()
print(x)



x = [1]
def test():
    x = [2]
test()
print(x)

x = [1]
def test():
    global x
    x = [2]
test()
print(x)


x = [1]
def test():
    x[0] = 2
test()
print(x)

"""
"""
def gamebc():
    print("0 , 1 , 2")
    games = lambda game : [print(count,row)for  count,row in enumerate(game)]
    games(game)

gamebc()
"""

























































































