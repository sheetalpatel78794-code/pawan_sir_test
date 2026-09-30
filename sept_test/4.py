start = int(input("Enter first no."))
end = int(input("Enter second no."))

count = 0
for i in range(start+1,end):
    n=2
    while n<=i//2:
        if i%n==0:
            break
        n=n+1

    if n>i//2 and i>1:
        print(i,end=" ")
        count +=1

print(f"Total prime number: {count}")
    

