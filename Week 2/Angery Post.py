import re

post = input("Post: ")
post = re.sub(r'[^\w\s]','',post)
counter = 0

for x in post.split():
  if x == x.upper():
    counter += 1

print(f"Number of angry words: {counter}")