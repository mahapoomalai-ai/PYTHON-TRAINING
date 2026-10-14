#Conditional Statements
#If Statement
a=10
if a>0:
    print("Positive")

#If-Else Statement
a = 5
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

#If-Elif-Else Statement
n = 0
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#Nested If Statement
age=int(input("Enter age:"))
if age>=18:
  if age>=21:
    print("Age is 21 or above")
  else:
    print("Age is between 18 and 20")
else:
  print("Below 18")

#Short-Hand If
n = 10
if n > 0: print("Positive")

#Multiple Conditions Using and
age = 20
if age >= 18 and age <= 60:
    print("Eligible")
else:
    print("Not Eligible")

#Match-Case Statement 
n = int(input())
match n:
    case 1: print("One")
    case 2: print("Two")
    case 3: print("Three")
    case _: print("Invalid")

#One value of each type from the user in the following order
integer_value = int(input())
float_value = float(input())
character_value = input()
long_value = int(input())
double_value = float(input())
print(integer_value)
print(float_value)
print(character_value)
print(long_value)
print(double_value)

#A floating-point number and prints successively rounded values, reducing the number of decimal places
n = float(input())
print(f"{n:.5f}")
print(f"{n:.4f}")
print(f"{n:.3f}")
print(f"{n:.2f}")
print(f"{n:.1f}")
print(int(n))

#Sum, Difference, Product, Division and Modulo
A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)

#ASCII
n = int(input())
print(chr(n))

#Update Counter
counter = int(input())
counter = counter + 5
counter = counter * 2
counter = counter - 3
print(counter)

#Greatest Among Three Numbers
a = int(input())
b = int(input())
c = int(input())
greatest = a if a > b and a > c else (b if b > c else c)
print(greatest)

#Character Digit to Integer
ch = input().strip().strip("'").strip('"')
print(int(ch))

#Personalized Greeting
name = input()
print(f"Hi {name}, welcome to the programming class!")

#Calculate Total and Average Marks
name = input()
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
total = m1 + m2 + m3 + m4 + m5
average = total / 5
print("Student Name:", name)
print("Total Marks:", total)
print(f"Average Marks: {average:.2f}")

#Shape Area Calculation
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
h = int(input())
square = a * a
rectangle = b * c
circle = 3.14 * d * d
triangle = 0.5 * e * h
print("Area of Square=", square, sep="")
print("Area of Rectangle=", rectangle, sep="")
print(f"Area of Circle={circle:.2f}")
print("Area of Triangle=", int(triangle) if triangle.is_integer() else triangle, sep="")

#Shape Perimeter Calculation Program
a = int(input())
b = int(input())
c = int(input())
d = int(input())
base1 = int(input())
side = int(input())
base2 = int(input())
square = 4 * a
rectangle = 2 * (b + c)
circle = 2 * 3.14 * d
triangle = base1 + side + base2
print(square)
print(rectangle)
print(f"{circle:.2f}")
print(triangle)

#Handling Mixed Inputs
a = int(input())
sentence = input()
print(a)
print(sentence)






