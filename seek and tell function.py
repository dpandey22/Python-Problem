f=open("C:/Users/LENOVO/Downloads/Assignments-20230922T174122Z-001/Assignments/Day 8/studentDetails.txt")
'''
f.seek(2)
content=f.read()

print(f.tell())
print(content)
'''


"""
seek function is being used to set the offset location, from where you want
to start reading the file, eg. if you want to skip till 10 character, then
have to use seek function, f.seek(10) it will start reading from 11th char.

"""

## if you want to read file from end then have use negative offset

f.seek(-10,2)  # here second parameter is reference
               #0 - beginning of file
               #1 - current position ( from current position)
               #2- end of line ( last in the file)
content=f.read()
print(content)


