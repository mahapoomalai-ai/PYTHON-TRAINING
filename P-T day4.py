#Count the number of digits
a=int(input())
count=0
if a==0:
    count=1
else:
    a=abs(a)
    while a > 0:
        count += 1
        a //= 10
print(count)

#Sum of Even Digits
n=int(input())
total=0
while n>0:
    digit=n%10
    if digit%2==0:
        total += digit
    n =n//10
print(total)

#Product of Digits
n=int(input())
product=1
while n>0:
  digits=n%10
  product=product*digits
  n=n//10
print(product)

#Reverse a Number
n=int(input())
rev=0
while n>0:
  last=n%10
  rev=rev*10+last
  n=n//10
print(rev)

#Palindrome Number
n=int(input())
temp=n
reverse=0
while n>0:
  digits=n%10
  reverse=reverse*10+digits
  n=n//10
if temp==reverse:
  print("Palindrome")
else:
  print("Not Palindrome")

#First Digit of a Number
n=int(input())
while n>=10:
  n=n//10
print(n)

#Count Zeros in a Number
n=int(input())
count=0
if n==0:
    count=1
else:
    while n>0:
        digit=n%10
        if digit==0:
            count+=1
        n=n//10
print(count)

#Armstrong Number
n=int(input())
temp=n
digit=0
while n>0:
  n=n//10
  digit+=1
n=temp
sum=0
while n>0:
  last=n%10
  sum=sum+last**digit
  n=n//10
if sum==temp:
  print("Armstrong")
else:
  print("Not Armstrong")

#Strong Number
n=int(input())
temp=n
total=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    total+=fact
    n=n//10
if total==temp:
    print("Strong")
else:
    print("Not Strong")

#Check Perfect Number
n=int(input())
sum=0
for i in range(1,(n//2)+1):
  if n%i==0:
    sum+=i
if sum==n:
  print("Perfect")
else:
  print("Not Perfect")
