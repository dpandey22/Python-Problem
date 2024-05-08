'''
lst=[5,6,9]
print(sum(lst))
print(max(lst))
print(min(lst))

def lst_mul(lst):
    result=1
    for ele in lst:
        result=result*ele
    return result

output=lst_mul([2,3,4])
print(output)



def str_com(lst):
    store=[]
    for ele in lst:
        if len(ele)>=2 and ele[0]==ele[-1]:
            store.append(ele)
    return store

output=str_com(['abc', 'xyz', 'aba', '1221'])
print(len(output))
'''

'''
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
'''
def last(n):
    return n[-1]
def sorted_lst(lst):
    return sorted(lst,key=last)

lst1=sorted_lst([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print(lst1)
'''

#------========================
############## Important methods of List #######################

lst=[4,5,6,7,8,9]

# to add element in the list
lst.append(15)
print(lst)

# Insert an element on specific position
lst.insert(2,'Vinay')
print("post insertion-",lst)

# to check the position of an element
print(lst.index(5))

# to check the occurance of any particular element-:
print(lst.count(5))

# to add other list in the lst at the last
lst.extend([45,62])
print("after extending",lst)

# to remove the element from the last in List
a=lst.pop()
print(a)

# to remove any particular element from the list

lst.remove('Vinay')
print('after removing vinay',lst)

# to reverse the list-:
lst.reverse()
print("reversed list is-:",lst)

# to sort a list in ascending or descending order
lst.sort(reverse=True)
print(lst)

# to find the minumum value of the list
print("the smallest values is-:",min(lst))

# to find the largest value of the list
print("the smallest values is-:",max(lst))

# to clear all elements from the list
lst.clear()
print("empty list",lst)


#########====== List Slicing ========== ###############
lst=[4,5,69,87,69]
'''
list[lower_bound:upper_bound]
lower_bound is inclusive but upper bound is exclusive from the result
'''
print(lst[1:3])

print(lst[:2]) # it will print till 1 index
print(lst[1:]) # it will start from 1 and will go till end
print(lst[:]) # it will print entire list
print(lst[-5:-1]) # negative slicing

print(lst[-5:3]) # Mixed slicing

# aggregaion function can be performed over the list except count
print("the total of the list element",sum(lst))
print("the average of the list element",(lst))






