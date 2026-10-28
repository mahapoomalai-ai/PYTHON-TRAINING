#Length of a string
n=input()
print(len(n))

#Join the Strings
a=input()
b=input()
print(a+" "+b)

#Compare the Strings
a=input()
b=input()
print(str(a==b).lower())

#First character of a string
n=input()
print(n[0])

#Last character of a string
n=input()
print(n[-1])

#Join first & last characters of a string
n=input()
print(n[0] + n[-1])

#Alphanumeric strings
s=input()
letters = any(c.isalpha() for c in s)
digits = any(c.isdigit() for c in s)
print(str(letters and digits).lower())

#Uppercase check
n=input()
print(str(n.isupper()).lower())

#Lowercase check
n=input()
print(str(n.islower()).lower())

#String lengths equal or not
a=input()
b=input()
print(str(len(a) == len(b)).lower())

#Reverse a String
n=input()
print(n[::-1])

#Split strings by comma
n=input()
words=n.split(',')
for word in words:
    print(word)

#Remove vowels
n=input()
result = ""
for ch in n:
    if ch.lower() not in "aeiou":
        result += ch
print(result)

#Remove vowels
result = ""
for ch in s:
    if ch.lower() not in "aeiou":
        result += ch
print(result)

#Reverse the character case
n=input()
print(n.swapcase())

#ascii value
n=input()
print(ord(n))

#Remove occurrences of a char
n=input()
ch=input()
print(n.replace(ch, ""))

#Search for a word
n=input()
word=input()
print(str(word in n).lower())

#Count vowels and consonants
s = input()
vowels = 0
consonants = 0
for ch in s.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print(vowels)
print(consonants)

#Palindrome check
s = input()
print(str(s == s[::-1]).lower())
