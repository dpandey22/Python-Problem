"""
Qns-1:
1. Write a class called Student with attributes student_id,student_name. Create 
   constructor with these attributes and 2 getter methods to get the student id and 
   student name.
"""
class Student():
    def __init__(self,student_id,student_name):
        self.stdname=student_name
        self.studentid=student_id
    def get_std_name(self):
        return self.stdname
    def get_std_id(self):
        return self.studentid

obj=Student(1,'Dinesh')
print(obj.get_std_id())
print(obj.get_std_name())


"""
2. Create another class WorkingStudent inheriting Student class created above. It will
   have one extra attribute monthly_salary and getter method to get the salary.
"""
class WorkingStudent(Student):
    def __init__(self,student_id,student_name,salary):
        super().__init__(student_id,student_name)
        self.salary=salary
    def get_salary(self):
        return self.salary

obj2=WorkingStudent(1,'Mukesh',4500)
print(obj2.get_salary())
print(obj2.get_std_name()) # creating the object and calling methods of parent class.

"""
4. What is polymorphism? Can same method be present in both parent and child class?

"""
# Polymorphism means behave multipurpose- one object can take more forms
## example of polymorphism- It calls the mehod as per object creation.
class a():
    def std_name(self):
        print("This is 1st class")
class b():
    def std_name(self):
        print("this is 2nd class")

obj1=a()
obj2=b()
bj1.std_name()
obj2.std_name()


"""
5. What is the difference between method overloading and method overriding? How
    is method overloading achieved in python?
"""
class std_parent():
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def addition(self):
        return str(self.id)+self.name
class std_child(std_parent):
    def __init__(self,id,name):
        super().__init__(id,name)
        
    def addition(self,num1,num2): # Method overidding
        self.num1=num1
        self.num2=num2
        return self.num1+self.num2

obj3=std_child(1,'Dinesh')
obj4=std_parent(2,'Mukesh')
print(obj3.addition(10,12))
print(obj4.addition())

################## Method overloading #######################
def sum_number(*args): # This takes multiple arguments
    # variable to store the sum of numbers    
    result = 0
    
    # accessing the arguments
    for num in args:
        result += num
    
    # Output
    print("Sum : ", result)

    
# Driver Code
if(__name__ == "__main__"):
    print("Similar to Method Overloading\n")
    print("Single Argument    ->", end = " ")
    sum_number(10)

    print("Two Arguments      ->", end = " ")
    sum_number(30, 2)

    print("Multiple Arguments ->", end = " ")
    sum_number(1, 2, 3, 4, 5)


"""
11. Write a program that takes list as input and the output should be list of
    running totals
    input = [2,3,4,5,6]
    output = [2,5,9,14,20]

"""

# Solution ####
lst=list(input("enter tha value for the list"))
running_sum=[]
sum=0
for ele in lst:
    sum=sum+int(ele)
    running_sum.append(sum)

print(running_sum)

    


        

