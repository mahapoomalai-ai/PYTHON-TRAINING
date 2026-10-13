#Shopping Bill Calculator
p1 = float(input("Enter first product price: "))
p2 = float(input("Enter second product price: "))
print("Total Bill:", p1 + p2)
print("Higher Price:", max(p1, p2))
print("Lower Price:", min(p1, p2))


#Student Mark Percentage
marks = float(input("Enter marks obtained: "))
total = float(input("Enter total marks: "))
percentage = (marks / total) * 100
print(f"Percentage: {percentage:.2f}%")

#Room Flooring Calculator
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")

#Delivery Distance Calculator
distance = float(input("Enter distance: "))
print("Whole-number distance:", int(distance))

#Packaging Calculator
items = int(input("Enter total items: "))
capacity = int(input("Enter box capacity: "))
boxes = (items + capacity - 1) // capacity
print("Boxes required:", boxes)

#Floor Tile Calculator
import math
area = float(input("Enter square floor area: "))
side = math.sqrt(area)
print(f"Side length: {side:.2f}")

#Access Permission Checker
permission = int(input("Enter permission value: "))
mask = int(input("Enter bit mask: "))
result = permission & mask
print("Resulting value:", result)

#Even or Odd Without Modulus
n = int(input("Enter an integer: "))
print("Even:", (n & 1) == 0)

#Shared Items Distribution
items = int(input("Enter total items: "))
teams = int(input("Enter number of teams: "))
print("Each team receives:", items // teams)
print("Items remaining:", items % teams)

#Coordinate Distance Calculator
import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Distance: {distance:.2f}")


