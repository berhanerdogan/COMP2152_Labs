# Question 6: Inventory Management System (Combined - All Collections)


inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}
priceList = []


print("=== Current Inventory ===")
for item, (price, quantity) in inventory.items():
    print(f"{item} - Price: {price}, Quantity: {quantity}")

    priceList.append(price)

print("")


electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
print(f"All product categories: {electronics | accessories}")
print(" ")


print("Price list:", priceList)
priceList.sort();
print("Sorted prices", priceList)
print("Lowest price:", priceList[0])
print("Highest price:", priceList[-1])
print(" ")

inventory["Mouse"] = (29.99,12)
inventory.popitem()

print("=== Final Inventory ===")
for item, (price, quantity) in inventory.items():
    print(f"{item} - Price: {price}, Quantity: {quantity}")


