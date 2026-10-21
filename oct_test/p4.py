'''Sets — Common and Unique Elements (5 Marks)

Given two lists, find:

Elements common to both lists.

Elements that appear in either list but not in both.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

Expected output:

Common elements: {30, 40}
Unique elements: {10, 20, 50, 60, 70}'''


list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

n1=len(list1)
n2=len(list2)

i1=i2=0

common=set()
unique=set()

while i1<n1 and i2<n2:
    if list1[i1]==list2[i2]:
        common.add(list1[i1])
        if list1[i1] in unique:
            unique.remove(list1[i1])
        i1+=1
        i2+=1
    elif list1[i1]<list2[i2]:
        unique.add(list1[i1])
        unique.add(list2[i2])
        i1+=1
    else:
        unique.add(list1[i1])
        unique.add(list2[i2])
        i2+=1

while i1<n1:
    unique.add(list1[i1])
    i1+=1

while i2<n2:
    unique.add(list2[i2])
    i2+=1

print(f"Common elements are {common}")
print(f"Unique elements are {unique}")

