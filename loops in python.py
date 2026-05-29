Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
#LOOP-repetition
#DRY - Don't Repeat Yourself
print(1)
1
print(2)
2
print(3)
3
print(4)
4
print(5)
5
for i in range(1,6):
    print(i)

1
2
3
4
5

for i in range(6):#by default range starts from 0
    print(i)

0
1
2
3
4
5

for i in range(1,6,1):
    print(i)

1
2
3
4
5
for i in range(1,6,2):
    print(i)

1
3
5

for i  in range(5,0,-1):
    print(i)

5
4
3
2
1

for i in reversed(range(1,6)):
    print(i)

5
4
3
2
1

#Break ,Continue and pass
#break  - break statement is used to transfer the control flow of program outside
#loop
for i in range(1,10000000000000000000001):
    if i==5:
        break
    else:
        print(i)

1
2
3
4
>>> 
>>> #continue : it is used to skip the current loop iteration
>>> for i in range(1,11):
...     if i%2==0:#remainder
...         continue
...     print(i)
... 
1
3
5
7
9
>>> 
>>> #pass
>>> for i in range(1,51):
...     pass
... 
>>> x = 1
>>> if x<0:
...     pass
... 
