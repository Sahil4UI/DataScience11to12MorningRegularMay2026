Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #List -List is python's ordered and mutable data collection
>>> x = [1,2,3,4,5]
>>> type(x)
<class 'list'>
>>> len(x)
5
>>> x.append(10)#it will store the value at the end
>>> x
[1, 2, 3, 4, 5, 10]
>>> x.insert(1,-20)
\
>>> x
[1, -20, 2, 3, 4, 5, 10]
>>> x[0]=100#update
>>> x
[100, -20, 2, 3, 4, 5, 10]
x.pop()#it will remove the last value
10
x
[100, -20, 2, 3, 4, 5]
x.pop(0)
100
x
[-20, 2, 3, 4, 5]
del x[0]
x
[2, 3, 4, 5]
x.remove(5)#remove by value
x
[2, 3, 4]
#list comprehension
\
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(x)):
    print(x[i],end=",")

1,2,3,4,5,6,7,8,9,10,
for value in x:
    print(value,end=",")

1,2,3,4,5,6,7,8,9,10,

x = [1,2,3,4,5]
x*3
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
