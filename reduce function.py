from functools import reduce
lst = ["Ramadas","Sam","Li","Tina","Priyanka"]
# what is the use of reduce fucntion- it is just compress the result set

lst_num=[1,2,5,6,3]

sum=reduce(lambda x,y:x+y,lst_num)
print("the total of all numbers-",sum)

#-- other mathod by using creating a function-
def sum_add(x,y):
    return x+y

sum1=reduce(sum_add,lst_num)
print("the ouput of function",sum1)

### combining the string from above list-:

def combine_str(x,y):
    return x+' '+ y

combine=reduce(combine_str,lst)
print("The combined string",combine)

#------- joining list with zip function=================
combined_lst=[]
lst_len=[7,3,2,4,8]
for a,b in zip(lst,lst_len):
    combined_lst.append(a)
    combined_lst.append(b)

print("combined List \n",combined_lst)



















    
