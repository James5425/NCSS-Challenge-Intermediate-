city = input("Enter a city file: ")
arr = []
with open(city) as f:
  f = f.readlines()
  for x in f:
    if x.strip() not in arr:
      arr.append(x.strip())

print("And the nominees are...")
for y in sorted(arr):
  print(f"🐦 {y}")