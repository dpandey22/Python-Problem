# opening file with context manager
'''
fw=open('C:/Users/LENOVO/Desktop/New folder/test1.txt','a')
with open("C:/Users/LENOVO/Downloads/Assignments-20230922T174122Z-001\
          /Assignments/Day 8/studentDetails.txt") as f:
    context=f.readlines()
    fw.write(context[6])
    fw.close()
'''
# in context manager no need to close the file, it will directly close the file

'''
2. Write a program using to read file studentDetails.txt and store the first 20 records 
   in a dictionary with name as key and other values as tuples. Sort the dictionary with 
   names in ascending order.
'''
# solution
'''
dict1={}
with open("C:/Users/LENOVO/Downloads/Assignments-20230922T174122Z-001/Assignments/Day 8/studentDetails.txt") as f:
    context=f.readlines()

    for ele in context[0:20]:
        ele1=ele.split()
        dict1[ele1[0]]=ele1[1:]

print(dict(sorted(dict1.items())))

'''
'''
5. What is a generator expression? How it is different from list? Create a generator object 
   for all odd numbers till 1000.
   Iterate through the generator to store only those elements in a list
   which are multiples of 10.
   How can we print all the values from the generator expression?
'''
'''
#Solution
def odd_generator(): # it is function of generator
    for i in range(1001):
        if i%2!=0:
            yield i

numbers=odd_generator()
print(next(numbers))
print(next(numbers))

## store only those records which are multiple of 10.
list1=[]
for i in numbers:
    
    if i%10==0:
        list1.append(i)

print(list1) # no any output because all numbers are odd.
'''
# another approach to create generator-:
gen_list=(i for i in range(10))
print(next(gen_list))
print(next(gen_list))

# it will be used when you deal with huge dataset.







