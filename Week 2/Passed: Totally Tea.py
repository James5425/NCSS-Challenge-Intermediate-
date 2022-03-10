t_name = input("Tour name: ")
city = input("Cities: ")

print(f"Announcing the national {t_name} tour!")
print("Visiting these cities...")
for x in city.split():
  print("🏙️", x)

print(f"Get excited for {t_name}!")