plant = input("Which plant did you survey? ").lower()
count = int(input("Count: "))

if "fern" in plant:
    print("Fantastic! Keep looking for ferns!")
elif "fern" not in plant:
    if count < 6:
        print(f"That's low. We'll put {plant} on the watch list.")
    elif count >= 6:
        print(f"Great! Recorded {count} {plant}" + "s", "in this area.")
