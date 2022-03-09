counter = 0
steamer = {}

while counter != 5:
  friend = input("Friend: ")
  steamer_rec = input("Which stream did they recommend? ")
  if steamer_rec in steamer:
    print("Someone else already recommended that.")
  else:
    steamer[steamer_rec] = friend
    print(f"{friend} recommended {steamer_rec}!")
    counter += 1

print("Playlist complete! Subscribe to:")
for x, y in steamer.items():
  print(f"{x}: recommended by {y}")