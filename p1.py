'''Q1. If-Else — Number Classification (5 Marks)

Write a program that accepts an integer and checks whether it is a Harshad number.

A number is a Harshad number if it is divisible by the sum of its digits.

Example:

Input: 18

Output: Harshad Number (18 is divisible by 1 + 8 = 9)'''

num = int(input("Enter a number:"))

temp = num
sum=0
while(num!=0):
    sum+=num%10
    num//=10

if temp%sum==0:
    print("it is a hashable no.")
else:
    print("it is not hashable no.")