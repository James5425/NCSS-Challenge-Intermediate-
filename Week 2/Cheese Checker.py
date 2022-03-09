cheeses = ['Cheddar', 'Bocconcini', 'Haloumi', 'Paneer', 'Gorgonzola', 'Mozzarella', 'Parmesan', 'Brie', 'Gruyere']

# Add your code after this.
cheese = input("Cheese: ")
if cheese in cheeses:
  print(f"{cheese} is a cheese!")
elif cheese in cheese:
  print(f"{cheese} might not be a cheese.")