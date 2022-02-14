def is_crowd(people):
    # Write your function here.
    if people >= 35:
        return "There's a crowd here!"
    elif people == 3:
        return "There's a crowd here!"
    else:
        return "There's no crowd here!"


# Write the rest of your program here.
print(is_crowd(int(input("Number of people: "))))