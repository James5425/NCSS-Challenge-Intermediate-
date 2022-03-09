players = ['Nicola', 'Penny', 'Dom', 'Nathan', 'Josie']
print(f"Friends: {players[0]}, {players[1]}, {players[2]}, {players[3]}, {players[4]}")
find = input("Who did you find? ")
if find in players:
    print(f"{find} has turned into a zombie!")
    players[players.index(find)] = "Zombie"
    print(f"Remaining players: {players[0]}, {players[1]}, {players[2]}, {players[3]}, {players[4]}")
else:
    print("Everyone is still in the game!")
    print(f"Remaining players: {players[0]}, {players[1]}, {players[2]}, {players[3]}, {players[4]}")