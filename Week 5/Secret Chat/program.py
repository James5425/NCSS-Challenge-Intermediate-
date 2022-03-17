dic = {}
tran = ""

sm = input("Secret Message: ")

with open("substitution.txt") as f:
    f = f.readlines()
    for x in f:
        dic[x[2]] = x[0]

for x in sm:
    if x.isalpha() == True:
        tran = tran + dic[x]
    else:
        tran = tran + x

print(f"Translation: {tran}")

