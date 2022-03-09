init_pop = int(input("Initial population: "))
final_pop = int(input("Final population: "))
counter = 0
while init_pop < final_pop:
    init_pop = init_pop + (0.14 * init_pop)
    counter += 1

print(f"It would take {counter} years for there to be {final_pop} cane toads.")