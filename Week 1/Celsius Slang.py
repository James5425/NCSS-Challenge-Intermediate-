def to_celsius(f):
  # Calculate the temperature in Celsius
    c = round((f - 32) * 5/9, 1)
    if c < 5:
        return f"{c} C - Crikey it's cold!"
    elif c >= 5 and c < 20:
        return f"{c} C - Getting a bit nippy!"
    elif c >= 20 and c < 35:
        return f"{c} C - You beaut beach weather!"
    else:
        return f"{c} C - Strewth, it's a scorcher!"

# Write the rest of your program here
print(to_celsius(float(input("Temp (F): "))))

