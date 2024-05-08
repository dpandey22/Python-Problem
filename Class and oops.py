## Class and objects-:
## There are three type of programming-
# Procedure oriented programming
# Object oriented programming (python and Java)
# functional programming ( just using function and lambda) ( it happened in only python)

'''
class students():
    #print("new") # just printing msg
    def set_name(self,name):        # self is bydefault input, and it refer object of this method
        self.a=name
    def set_subject(self,subject):
        self.sub=subject
    def get_name(self):              # this is the instance method
        return self.a            # this is the instance variable 
    def get_sub(self):
        return self.sub
    

# to access this class we need to create a object-
obj=students()
obj.set_name('Dinesh')
print(obj.get_name())
obj.set_subject("SQL")
print(obj.get_sub())
'''

class students1():
    def set_name(self,name):
        self.a=name
    def get_name(self):
        return self.a

lst=[]
obj=students1()
lst.append(obj)

for obj1 in lst:   # we can access function through list
    print(obj1.set_name('Vinay'),obj1.get_name())



