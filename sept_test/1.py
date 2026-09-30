unit = int(input("Enter unit :"))

if unit<=100 and unit>0:
    bill = unit *5
    print(f"bill {bill}")

elif unit<=200 and unit>100:
    bill = 100 *5 +(unit-100)*7
    print(f"bill {bill}")

elif unit<=400 and unit>200:
    bill = (100 *5) +(100*7)+(unit-200)*10
    print(f"bill {bill}")

elif unit<=600 and unit>400:
    bill = (100 *5 )+(100*7)+(200*10)+(unit-400)*12
    print(f"bill {bill}")

print(f"bill {bill}")