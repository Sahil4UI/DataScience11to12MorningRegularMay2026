Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
#List:List is Python's Ordered and mutable data collection
#ordered - indexing , mutable - >change(store,edit,delete)
x = [1,2,3,4,5]
type(x)
<class 'list'>
len(x)
5
#indexing
x
[1, 2, 3, 4, 5]
x[0]
1
x[1]
2
x[-1]
5
#slicing
x
[1, 2, 3, 4, 5]
x[0:3]
[1, 2, 3]
x[2:5]
[3, 4, 5]
x[:3]
[1, 2, 3]
x[3:]
[4, 5]

#nested indexing
x = [1,2,3,[4,5,6,7]]
x[3]
[4, 5, 6, 7]
>>> x[3][2]
6
>>> 
>>> #list methods
>>> x
[1, 2, 3, [4, 5, 6, 7]]
>>> x = [1,2,3,4,5]
>>> x.append(10)
>>> x
[1, 2, 3, 4, 5, 10]
>>> x.append(20)
>>> x
[1, 2, 3, 4, 5, 10, 20]
>>> x.insert(0,-10)
>>> x
[-10, 1, 2, 3, 4, 5, 10, 20]
>>> x.pop()
20
>>> x
[-10, 1, 2, 3, 4, 5, 10]
x.pop()
10
x.pop(0)
-10
x
[1, 2, 3, 4, 5]
x.remove(5)
x
[1, 2, 3, 4]
del x[0]
x
[2, 3, 4]
x.clear()
x
[]
x = [10,56,7,34,0,-10,9.3]
min(x)
-10
max(x)
56
sum(x)
106.3
x.sort()
x
[-10, 0, 7, 9.3, 10, 34, 56]
x.sort(reverse=True)
x
[56, 34, 10, 9.3, 7, 0, -10]
x
[56, 34, 10, 9.3, 7, 0, -10]
x.index(56)
0
x.append(56)
x
[56, 34, 10, 9.3, 7, 0, -10, 56]
x.index(56)
0
x.index(56,0)
0
x.index(56,1)
7
x.count(56)
2
x = [1,2,3,4,5]
y = [6,7,8,9,10]
x.extend(y)
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y
[6, 7, 8, 9, 10]
y*2
[6, 7, 8, 9, 10, 6, 7, 8, 9, 10]
#list comprehension
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#using loop on list
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for value in x:
    print(value)

1
2
3
4
5
6
7
8
9
10
