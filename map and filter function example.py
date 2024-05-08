'''
7. lst = ["30 days ago","5 days ago","7 days ago"]
   Use map function with lambdas to create a new list with only numeric values
'''
# Solution-:

lst = ["30 days ago","5 days ago","7 days ago"]
new_lst=list(map(lambda x:x[0],lst)) # have used list because map return a object
print(new_lst)

# solution 2-:

def onlyNumeric(name):
    return name[0]

lst = ["30 days ago","5 days ago","7 days ago"]
new_lst2=list(map(onlyNumeric,lst))
print("second methond of map function")
print(new_lst2)

test=onlyNumeric(lst)
print("only fucntion",test)

# Definition-:
'''
Map in Python is a function that works as an iterator to return a result after
applying a function to every item of an iterable (tuple, lists, etc.).
It is used when you want to apply a single transformation function to all the
iterable elements.
The iterable and function are passed as arguments to the map in Python.
'''

def filter_fun(name):
    if name.endswith('s'):
        return name

lst=['Vinay','Vines','Lavles','Kumar','Vishes']

newlist=list(filter(filter_fun,lst)) 
print(newlist)

# filter and map function works just like an iterator-















