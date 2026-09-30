first_no= int(input("Enter a first number:"))
second_no = int(input("Enter a second number:"))

operation = input("Enter a operation:")

match operation :

    case "+":
        sum = first_no +second_no
        print(f"sum = {sum}")

    case "-":
        sub = first_no - second_no
        print(f"sub = {sub}")

    case "*":
        mult = first_no * second_no
        print(f"mult = {mult}")

    case "/":
        if second_no>0:
            div = first_no/second_no
            print(f"divide = {div}")
        else:
            print("Cannot be divide by zero:")
    case "%":
        rem = first_no%second_no
        print(f"remainder {rem}")

    case _:
        print("invalid operation")


            
