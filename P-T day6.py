#Print Array Elements
n=int(input())
arr=list(map(int, input().split()))
for i in arr:
    print(i,end=" ")

#Sum of Array Elements
n=int(input())
arr=list(map(int, input().split()))
total=sum(arr)
print(total)

#Sum of Odd and Even Elements in an Array
n=int(input())
arr=list(map(int, input().split()))
evencount=0
oddcount=0
for i in arr:
    if i % 2 == 0:
        evencount+=i
    else:
        oddcount+=i
print(evencount,oddcount)

#Sum of Elements at Odd and Even Indices in an Array
n = int(input())
arr = list(map(int, input().split()))
evencount=0
oddcount=0
for i in range(n):
    if i % 2 == 0:
        evencount+= arr[i]
    else:
        oddcount+= arr[i]
print(evencount, oddcount)

#Find Maximum Element in an Array
n=int(input())
arr=list(map(int, input().split()))
maximum=max(arr)
print(maximum)

#Find Minimum Element in an Array
n=int(input())
arr=list(map(int, input().split()))
minimum=min(arr)
print(minimum)

#Find Maximum Odd and Even Elements in an Array
n = int(input())
arr = list(map(int, input().split()))
even = []
odd = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
if len(even) > 0:
    print(max(even))
else:
    print("None")
if len(odd) > 0:
    print(max(odd))
else:
    print("None")

#Difference Between Sum of Odd and Even Elements in an Array
n=int(input())
arr=list(map(int, input().split()))
odd=0
even=0
for i in arr:
    if  i%2 == 0:
        even+=i
    else:
        odd+=i
difference=odd-even
print(difference)

#Check if a Key Number Exists in an Array
n=int(input())
arr=list(map(int,input().split()))
key=int(input())
if key in arr:
  print("Yes")
else:
  print("No")

#Find Index of a Key Number in an Array
n=int(input())
s=list(map(int,input().split()))
key=int(input())
if key in s:
  print(s.index(key))
else:
  print(-1)





