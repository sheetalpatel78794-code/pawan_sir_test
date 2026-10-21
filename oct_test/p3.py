'''Q3. Lists — Second-Largest Distinct Element (5 Marks)

Given a list of integers, find the second-largest distinct element without using sort(), sorted(), or max().

numbers = [12, 45, 7, 45, 30, 22, 30]

Expected output: 30'''

A = [12, 45, 7, 45, 30, 22, 30]
result = []
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[j]<A[i]:
            A[i],A[j]=A[j],A[i]

print(A)

for i in range(len(A)):
    if A[i] in result:
        continue
    else:
        result.append(A[i])

print(result)
print(result[-2])