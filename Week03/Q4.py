# Question 4: Class Attendance (Sets - Uniqueness and Operations)

mondayClass = {"Alice", "Bob", "Charlie", "Diana"}
wednesdayClass = {"Bob", "Diana", "Eve", "Frank"}

mondayClass.add("Grace")

intersection = mondayClass & wednesdayClass
union = mondayClass | wednesdayClass
difference = mondayClass - wednesdayClass
sDifference = mondayClass ^ wednesdayClass

print("Monday class:", mondayClass)
print("Wednesday class:", wednesdayClass)
print("Attended both classes:", intersection)
print("Attended either class:", union)
print("Only Monday:", difference)
print("Only one class (not both):", sDifference)

print("Is Monday subset of all students?", mondayClass <= union)
