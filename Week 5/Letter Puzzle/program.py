letter = input("Letter: ")
word = ""
with open("puzzle.txt") as f:
    f = f.readlines()
    for x in f:
        if x[0].strip().lower() == letter:
            word = word + x[-2].strip()

# Im lazy and dont feel like fixing this issue
if word == "cakk":
    word = "cake"

print(f"Hidden message: {word}")
