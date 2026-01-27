# Question 3: Coordinate System (Tuples - Creation and Unpacking)

point1 = (3,5)
point2 = (7,2)
(x1,y1) = point1
(x2,y2) = point2
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
tuple = tuple("PYTHON")

print(f"Point 1: {point1}\nPoint 2: {point2}")
print(f"x1 = {x1}, y1 = {y1}\nx2 = {x2}, y2 = {y2}")
print("Distance between points:", distance)
print("Characters tuple:", tuple)

for char in tuple:
    print(char)


