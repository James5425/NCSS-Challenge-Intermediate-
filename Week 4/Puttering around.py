dic = {}

player = input("Player: ")
while player:
  score = int(input("Score: "))
  if player in dic:
    dic[player] = dic[player] + score
  else:
    dic[player] = score
  player = input("Player: ")

print("Final Results:")
for x, y in dic.items():
  print(f"{x}: {y}")