# Question 2: Shopping Cart (Lists - Searching and Removal)

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("We have", apple_count, "apples")
print("Index of milk:", cart.index("milk"))
cart.remove("apple") # first occurance will be removed
print("Removed item using pop:", cart.pop()) # default pop will be last item
print("Is banana in the cart?", "banana" in cart)
print("Final cart:", cart)


