'''Q5. Dictionaries — Word Frequency (5 Marks)

Write a program to count the frequency of each word in a sentence using a dictionary. Treat uppercase and lowercase words as the same.

sentence = "Python is easy and Python is powerful"

Expected output:

{
    'python': 2,
    'is': 2,
    'easy': 1,
    'and': 1,
    'powerful': 1
}'''

sentence = "Python is easy and Python is powerful"
list = []
list +=sentence.split()
print(list)
dictionary = {}
for word in list:
    if word in dictionary:
        dictionary[word]=dictionary[word]+1
    else:
        dictionary[word]=1

print(dictionary)

    
        