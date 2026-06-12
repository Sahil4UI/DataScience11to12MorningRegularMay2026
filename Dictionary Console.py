Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #Dictionary
>>> data = {"id":101,"name":"amit"}
>>> #dictionary is pythons unordered and mutable data collection
>>> #unordered - no indexin
>>> #indexing
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data[0]
KeyError: 0
>>> 
>>> x
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x
NameError: name 'x' is not defined
data
{'id': 101, 'name': 'amit'}
#how to add new key value pair
data["contact"]=9876543210
data
{'id': 101, 'name': 'amit', 'contact': 9876543210}
#dictionary cannot contain duplicate key
data["id"]=102
data
{'id': 102, 'name': 'amit', 'contact': 9876543210}

#how to delete values from dictionary
data
{'id': 102, 'name': 'amit', 'contact': 9876543210}
data.popitem()#it will remove last key value pair
('contact', 9876543210)
data
{'id': 102, 'name': 'amit'}

del data["id"]
data
{'name': 'amit'}

x = {'id': 102, 'name': 'amit', 'contact': 9876543210}
x["id"]
102
x["name"]
'amit'
x["contact"]
9876543210

x.get("id")
102

x
{'id': 102, 'name': 'amit', 'contact': 9876543210}
x.keys()
dict_keys(['id', 'name', 'contact'])
x.values()
dict_values([102, 'amit', 9876543210])
x.items()
dict_items([('id', 102), ('name', 'amit'), ('contact', 9876543210)])

x
{'id': 102, 'name': 'amit', 'contact': 9876543210}
for key in x:
    print(key,"=>",x.get(key))

id => 102
name => amit
contact => 9876543210

