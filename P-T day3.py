#Loop statement
#for Loop
for i in range(1, 6):
    print(i)

#while Loop
i = 1
while i <= 5:
    print(i)
    i += 1

#Do-While Loop
while True:
    n = int(input("Enter a number: "))
    print("Number:", n)
    if n == 5:
        break

#Nested Loop
for i in range(2):
    for j in range(2):
        print(i, j)

#Sum of Numbers Until Zero
total = 0
while True:
    n = int(input())
    if n == 0:
        break
    total += n
print(total)

#Reverse a Number
n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

#Break Statement
for i in range(1, 11):
    if i == 6:
        break
    print(i)

#Continue Statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#while loop, for loop, if-elif-else, list, and functions
students = []
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Show Topper")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
  if choice == 1:
        name = input("Enter student name: ")
        mark1 = int(input("Enter mark 1: "))
        mark2 = int(input("Enter mark 2: "))
        mark3 = int(input("Enter mark 3: "))
    total = mark1 + mark2 + mark3
        average = total / 3
        student = {
            "name": name,
            "total": total,
            "average": average
        }
        students.append(student)
        print("Student added successfully!")
  elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            for s in students:
                print("\nName:", s["name"])
                print("Total:", s["total"])
                print("Average:", round(s["average"], 2))
              if s["average"] >= 90:
                    print("Grade: A")
                elif s["average"] >= 75:
                    print("Grade: B")
                elif s["average"] >= 50:
                    print("Grade: C")
                else:
                    print("Grade: FAIL")
              elif choice == 3:
        search_name = input("Enter name to search: ")
        found = False
      for s in students:
            if s["name"].lower() == search_name.lower():
                print("Student Found!")
                print("Name:", s["name"])
                print("Total:", s["total"])
                print("Average:", round(s["average"], 2))
                found = True
                break
              if not found:
            print("Student not found.")
      elif choice == 4:
        if len(students) == 0:
            print("No records available.")
        else:
            total_average = 0
        for s in students:
                total_average += s["average"]
          class_average = total_average / len(students)
            print("Class Average:", round(class_average, 2))
        elif choice == 5:
        if len(students) == 0:
            print("No records available.")
        else:
            topper = students[0]
            for s in students:
                if s["total"] > topper["total"]:
                    topper = s
                  print("Class Topper:", topper["name"])
                  print("Total Marks:", topper["total"])
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")

#Identify the Nature of a Number
n = int(input())
if n > 0:
    print("POSITIVE")
elif n < 0:
    print("NEGATIVE")
else:
    print("ZERO")

#Explore Math Functions
import math
a = float(input())
b = int(input())
c = int(input())
d = int(input())
print(math.floor(a))
print(math.ceil(a))
print(round(a))
print(math.sqrt(b))
print(math.pow(c, d))

#Smallest of Four Numbers
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a, b, c, d))

#Truncate to Two Decimal Places
n = float(input())
print(int(n * 100) / 100)

#Find Second Maximum Number
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("No second max")
elif a >= b and a >= c:
    print(max(b, c))
elif b >= a and b >= c:
    print(max(a, c))
else:
    print(max(a, b))

#Triangle Angle Validation
a = int(input())
b = int(input())
c = int(input())
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("VALID")
    if a == b == c:
        print("EQUILATERAL")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT VALID")

#Number to Word
n = int(input())
words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]
print(words[n])

#Vowel or Consonant
ch = input().lower()
if ch in "aeiou":
    print("vowel")
else:
    print("consonant")

#Leap Year Checker
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("yes")
else:
    print("no")

#Fun Grade Calculator
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = (a + b + c + d + e) / 5
if avg >= 90:
    print("Excellent!")
elif avg >= 80:
    print("Great Job!")
elif avg >= 70:
    print("Good Effort!")
elif avg >= 50:
    print("Keep Trying!")
else:
    print("Better Luck Next Time!")

#Train Berth Type Finder
t = int(input())
for i in range(t):
    n = int(input())
    r = n % 8
    if r == 1 or r == 4:
        print("LB")
    elif r == 2 or r == 5:
        print("MB")
    elif r == 3 or r == 6:
        print("UB")
    elif r == 7:
        print("SL")
    else:
        print("SU")

#Electricity Bill Calculator
units = float(input())
if units <= 50:
    bill = units * 1
elif units <= 150:
    bill = 50 + (units - 50) * 2
elif units <= 250:
    bill = 250 + (units - 150) * 3
else:
    bill = 550 + (units - 250) * 4
if bill > 150:
    bill += bill * 0.20
print(int(bill) if bill.is_integer() else bill)
