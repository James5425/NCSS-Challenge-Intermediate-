def sale_price(original, discount):
    return round((1 - discount/100) * original, 2)

print(input("Product: ")+ " on sale for "+ "$"+str(sale_price(float(input("Original price ($): ")), float(input("Discount (%): "))))+".")