Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #String - it is python's ordered and immutable data collection
>>> x = "welcome to python"
>>> type(x)
<class 'str'>
>>> x = 'Welcome to "Python"'
>>> print(x)
Welcome to "Python"
>>> x = "Welcome to \"Python\""
>>> print(x)
Welcome to "Python"
>>> #multi line String
>>> x = '''Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
... To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.'''
#Indexing and Slicing
x="hey python"
x[0]
'h'
x[1]
'e'
x[-1]
'n'
x[-2]
'o'
x
'hey python'
x[0:5]
'hey p'
x[0:5:1]
'hey p'
x[0:8:2]
'hypt'
x[:8:2]#by defaulk
'hypt'
#by default it will starts from 0
x[::2]
'hypto'
x[:]
'hey python'
x[::-1]#reverse
'nohtyp yeh'
#String methods
x
'hey python'
x = "Welcome To Python"
x.upper()
'WELCOME TO PYTHON'
x.lower()
'welcome to python'
x.capitalize()
'Welcome to python'
x.title()
'Welcome To Python'
x
'Welcome To Python'
x.swapcase()
'wELCOME tO pYTHON'
x
'Welcome To Python'
x = "anushka"
len(x)
7
x.center(19)
'      anushka      '
x.center(8)
'anushka '
x.center(20,"*")
'******anushka*******'
x = '******anushka*******'
x.strip("*")
'anushka'
x = "hey welcome to String"
x.find("h")
0
x.find("e")#first occurence
1
x.rfind("e")#last occurence
10
x.find("e",2)
5
x.index("e",2)
5
x.find("X")
-1
x.index("X")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'hey welcome to String'
x.count("e")
3
y = "anushka"
y.zfill(10)
'000anushka'
x
'hey welcome to String'
y
'anushka'
y.isalpha()
True
y.isalnum()
True
y.isdigit()
False
y.isupper()
False
