num = int(input("Enter a number:"))

temp = num 
count = 0
rev = 0
sum = 0
larger_digit=0
smaller_digit=9

while(temp>0):
    rem = temp%10
    rev = rev*10+rem
    temp = temp//10
    count += 1
    sum = sum + rem
    if larger_digit<rem:
        larger_digit = rem
    if smaller_digit>rem:
        smaller_digit = rem

print(f"Sum of digit {sum}")
print("No of digit:",count)
print(f"largest_digit {larger_digit}")
print(f"smallest_digit {smaller_digit}")
if rev == num:
    print("Palindrome ")

else:
    print("Not Palindrom")

