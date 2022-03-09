q1 = input("Why does the sun rise in the east? ")
if "i don't know" in q1.lower():
    print("Let's find out!")
else:
    print("hmm...")
    by = input("But why? ")
    if "i don't know" in by.lower():
        print("Let's find out!")
    else:

        while "i don't know" not in by.lower():
            print("hmm...")
            by = input("But why? ")

        print("Let's find out!")