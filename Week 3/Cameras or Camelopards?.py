counter = 0
arr = []
while counter != 3:
  ss = input("Shop stock: ")
  if "cam" in ss.lower():
    counter += 1
    arr.append(ss)
  else:
    pass

arr.sort(reverse=True)
print(f"Proposals: {arr[0]}, {arr[1]}, {arr[2]}")