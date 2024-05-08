class MyList:
    def __init__(self):
        self.items=[]
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,value):
        self.items.append(value)
    

my_list=MyList()
my_list[0]=25
my_list[1]=30

print(my_list[0],my_list[1])


'''
class MyList:
    def __init__(self):
        self.items=[]

my_list=MyList()
#my_list[0]=25
#print(my_list[0])


print(dir(MyList))
'''
