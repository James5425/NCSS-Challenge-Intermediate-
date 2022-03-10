time_tables = int(input("Times table: "))
steps = int(input("Step: "))
g = 3
while g <= 12:
  print(f"{time_tables} x [ ] =", time_tables * g)
  g += steps


