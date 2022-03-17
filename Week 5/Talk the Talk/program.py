i = input("Speech file: ")

with open(i, "r") as f:
    text = f.read().split()

start = 0
sent = ""
while start != 200:
    sent = sent + " " + text[start]
    start += 5

sent = sent.strip()
print(sent)
