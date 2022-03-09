print("Thanks all for coming to donut donation day!")
list = []
total = 0
donate = input("Who's next to donate? ")
while donate:
    amount = float(input("How much are you donating? "))
    total = total + amount

    if donate in list:
        print(f"Another generous donation from {donate} of ${amount:.2f}!")
    else:
        print(f"Thanks {donate}! A first donation of ${amount:.2f}!")
        list.append(donate)
    donate = input("Who's next to donate? ")

print(f"That's it folks! We raised ${total:.2f}!")
print("All thanks to our delicious donors:")
for x in sorted(list):
    print(f"🍩 {x}")
