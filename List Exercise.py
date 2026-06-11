'''q1. Write a program to find the largest element from list without
using max function'''
'''
x = [90,435,6,0,19,3,4,6.8,9876]

largest = x[0]

for value in x[1:]:
    if value>largest:
        largest = value
        
print(largest)
'''
'''
q2. write a program to sort the list in ascending order
without using sort method.'''
'''
x = [0,4,6,-10,40,0.2,404]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)
'''     


'''Q3.Write a program to remove duplicates from list.
x = [1,1,1,1,2,2,2,2,3,3,3]
output : [1,2,3]'''
'''
x = [1,1,1,1,2,2,2,2,3,3,3]
y = []

for item in x:
    if item not in y:
        y.append(item)

print(y)
'''
'''
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''
x = ['abc', 'xyz', 'aba', '1221']
count = 0
for value in x:
    if value[0]==value[-1]:
        count+=1
print(count)
    











        
