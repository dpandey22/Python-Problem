import csv
lst=[]

# Example of CSV Reader
'''
with open("C:\\Users\\LENOVO\\Downloads\\Assignments-20230922T174122Z-001\\Assignments\Day 12\\DataEngineering.csv") as f:
    reader=csv.reader(f)
    #print(next(reader)) # csv.reader- create a generator and we can access values by using next keyword or for loop.
    #print(next(reader))
    for ele in reader:
        lst.append(ele)

print(lst)
'''

# See the example of DictReader()
'''
with open("C:\\Users\\LENOVO\\Downloads\\Assignments-20230922T174122Z-001\\Assignments\Day 12\\DataEngineering.csv") as f:
    dreader=csv.DictReader(f)
    print(next(dreader))
    for row in dreader:
        print(row['salary'])
'''

'''
6.Create a generator function that will read the csv file DataEngineer.csv
  and return the content of column 'Skill set'. Yield only those skill
  sets which is having word 'python' in it
  Call the generator function and save all the values in a list and
'''

def file_generator():
    lst=[]
    with open("C:\\Users\\LENOVO\\Downloads\\Assignments-20230922T174122Z-001\\Assignments\Day 12\\DataEngineering.csv") as f:
        dreader=csv.DictReader(f)
        for ele in dreader:
            if int(ele['salary'])>1000:
                lst.append(ele['salary'])
    return lst


print(file_generator())

'''
7.Create a class DataEngineer with atrributes Date, Company, JobTitle, Experience. 
  Read the data from DataEngineer.csv file and create objects. Number of objects
  would be the number of rows in the csv file except the hearders.
'''

class dataEngineer():
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    with open("C:\\Users\\LENOVO\\Downloads\\Assignments-20230922T174122Z-001\\Assignments\Day 12\\DataEngineering.csv") as f:
        reader=csv.reader(f)

obj=dataEngineer()
for ele in obj:
    print(ele)

# we need to ask this questions ###


