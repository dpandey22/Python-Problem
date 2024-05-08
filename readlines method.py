'''
9. Open the file StudentDetails.txt file and read the content using readlines method
   and store it in one variable.
   Open another file in write mode and write that variable to the file.
'''
f=open("C:/Users/LENOVO/Downloads/Assignments-20230922T174122Z-001/Assignments/Day 8/studentDetails.txt")
new_content=[]
fw=open("C:/Users/LENOVO/Desktop/New folder/test.txt",'r+')

content=f.readlines() # it will create a list with non printable character
for i in range(len(content)):
    fw.write(content[i]) # it will write line by line as it was in existing file.
fw.close()
f.close()
    

'''
fw.write(str(content))
fw.close()
f.close()
'''


    
