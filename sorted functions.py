lst=[(9,1),(10,5),(11,3),(96,2),(45,1)]

#qns- sort the list by last element of each tuple
print("List before sorting\n",lst)
lst1=sorted(lst,key=lambda x:x[-1])
print(lst1)

## secdond way using function-:

def last(n):
    return n[-1]
lst2=sorted(lst,key=last)
print(lst2)
