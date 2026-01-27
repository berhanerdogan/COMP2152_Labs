# Question 5: Contact Book (Dictionaries - Basic Operations)

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-999"
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

names = dict.keys(contacts)
numbers = dict.values(contacts)
length = len(contacts)
print("All names:", names)
print("All numbers:", numbers)
print("Total contacts:", length)