'''Write a program to print all prime numbers between 1 and 100. Do not use any built-in prime-checking function.'''

for i in range(2,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count<=2:
        print(i,end=" ")


