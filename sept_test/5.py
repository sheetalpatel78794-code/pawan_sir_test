



python = int(input("Enter a marks of python:"))
database = int(input("Enter a marks of database:"))
programming = int(input("Enter a marks of programming:"))

average = (python + database+programming)/3

while True:
    print("Enter 1 for the marks enter:")
    print("Enter 2 for the average:")
    print("Enter 3 for higest mark:")
    print("Enter 4 for lowest mark:")
    print("Enter 5 for result:")
    print("Enter 6 for exist:")

    choice = int(input("Enter choice"))
    match choice :

        case 1:
            print(f"python {python}")
            print(f"database {database}")
            print(f"programming {programming}")

        case 2:
        
            print(f"Average {average}")

        case 3:
            if (python>database and python>programming):
                print(f"python {python}")
            elif (database>programming):
                print(f"database {database}")
            else:
                print(f"programming {programming}")

        case 4:
                if (python<database and python<programming):
                    print(f"python {python}")
                elif (database<programming):
                    print(f"database {database}")
                else:
                    print(f"programming {programming}")
        
        case 5:
            if (python>=40 and database>=40 and programming>=40 and average>=50):
                print(f"Pass")
            else:
                print(f"Fail")

        case 6:
            print(f"Ending of the program")
            break

        case _:
            print("Invalid input:")
        


