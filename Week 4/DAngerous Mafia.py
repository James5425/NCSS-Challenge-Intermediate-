def buy_skins(dam):
  # Finish the function to convert DAM to skins
  pass

# Write the rest of your program here
dic = {}
print("Who's playing Dangerous Mafia?")
name = input("Name: ")
while name:
    DAM = int(input("Starting number of DAM: "))
    tot = DAM / 40
    dic[name] = DAM
    print(f"{name}'s here, starting with {int(tot)} skins worth of DAM!")
    name = input("Name: ")

print("Let's play!")
playered = input("Who played? ")
while playered:
    lost = int(input("DAM won/lost: "))
    if playered in dic:
        dic[playered] = dic[playered] + lost
    else:
        dic[playered] = lost
    playered = input("Who played? ")

print("End of the game! Let's see how everyone did!")
for x, y in dic.items():
    print(f"{x} can buy {int(y / 40)} skins.")