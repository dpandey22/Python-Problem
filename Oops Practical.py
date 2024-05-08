# Object oriented Programming
# functional programming
# procedure oriented programming

class practice():
    def set_name(self,name): # instance method
        self.a=name #instance variable
    def get_name(self):
        return self.a

obj=practice()
obj.set_name('dinesh')
print(obj.get_name())

## anohter way of calling function

### accessing function and methods through list
lst=[]
lst.append(obj) # it will store all method inside the list

for obj1 in lst:
    obj1.set_name('Rahul')
    print(obj1.get_name())
    

####################### using class variable==============
# class variable can accessed through both class name or object name

class access_variable():
    no_of_student=5 # class variable or static variable
    def set_name(self,name): # self that is refer an object
        self.a=name
    def get_name():
        return self.a

obj1=access_variable()
print(access_variable.no_of_student)
obj1.no_of_student=6 # here it is creating new variable

#We can access class variables by class name or object reference
#print(id(access_variable.no_of_student),id(obj1.no_of_student))


class check_diff():
    def __init__(self,age):
        self.age=age

    def compare(self,other): # here other means other object
        if self.age==other.age:
            print("they are same")
        else:
            print("they are different")

s1=check_diff(25)
s2=check_diff(35) # we can pass the constructure value in this way as well.

s1.compare(s2)

print("============ class check_diff1()============")
class check_diff1():
    def set_age(self,age):
        self.age=age
    def compare(self,other): # here other means other object
        if self.age==other.age:
            print("they are same")
        else:
            print("they are different")

s1=check_diff1()
s2=check_diff1()
s1.set_age(35)
s2.set_age(40)
s1.compare(s2)


#################### Static Method, class method and Instance methods++++++++++++

class class_methods():
    amount=500
    def set_deposit(self,amt): # this is instance method
        self.amt=amt
        class_methods.amount=class_methods.amount-amt
    def get_balance(self):
        return class_methods.amount

    @classmethod
    def new_method(cls):
        return cls.amount

    @staticmethod
    def only_print():
        print("Now it is static method")
        print("class variable-",class_methods.amount)

s1=class_methods()
s1.only_print()

s1.set_deposit(200)

print(s1.get_balance())
print(class_methods.new_method())


import socket
def find_ip():
    """This is a program which will print IP address of your system"""
    ip = socket.gethostbyname(socket.gethostname())
    return ip

a=find_ip()
print("the IP address is-",a)


def mul_num(l):
    """This function will return product of all numeric elements of a list"""
    mul = 1
    for i in l:
        if type(i) == int or type(i) == float:
            mul = mul * i
    return mul

num=mul_num([10,2,30])
print("multiplication",num)

























        


