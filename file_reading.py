## reading file----

f=open("C:/Users/LENOVO/Downloads/Assignments-20230922T174122Z-001/Assignments/Day 8/studentDetails.txt")

#content=f.read()
#print(content)

#content=f.readline()
#print(content)

#content=f.readlines()
#print(content[0])

## reading lines and creating dictionary
"""
5. Write a program to read the content of file named StudentDetails.
  Each line in the file contains record of a student(ID,Name,EnrolledMonth,EnrolledYear)
  Store all the student details in a dictionary using ID as key and value as 
  Name,EnrolledMonth and EnrolledYear in a tuple.
"""
# solution of qns 5 #
'''dict1={}
content=f.readlines()
for ele in content:
    lst=ele.split()
    dict1[lst[0]]=tuple(lst[1:])
print(dict1)
'''
print(f.readline())
print(f.tell()) # it tells the current position of cursor while working with file.
print(f.seek(5,2)) # need to read it form YT or google

"""
Qns-9. Open the file StudentDetails.txt file and read the content using readlines method
   and store it in one variable.
   Open another file in write mode and write that variable to the file.
"""



