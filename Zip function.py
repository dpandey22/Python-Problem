# Zip function and its limitation-:
lst = ["Ramadas","Sam","Li","Tina","Priyanka"]
lst_len=[7,3,2,4,8]

# 1st method of using Zip()
combined_lst=list(zip(lst,lst_len))
print("using 1st method",combined_lst)
combined_dict=dict(zip(lst,lst_len))
print("dictiionay using zip",combined_dict)

# another method using loops

combined_lst_loop=[]
for a,b in zip(lst,lst_len):
    combined_lst_loop.append(a)
    combined_lst_loop.append(b)

print("==========through loop \n",combined_lst_loop)
    
combined_dict_loop={}
for a,b in zip(lst,lst_len):
    combined_dict_loop[a]=b

print("************Dictionary through loop \n", combined_dict_loop)


## Limiation of Zip

lst1=[4,5,6,9]
lst2=['a','b','c']

limitation=list(zip(lst2,lst1))
print(limitation)

# there is limitaion, if no of element is not equal then it will skipp the value
#that does not have any combination, for this we need to import zip_longest()

from itertools import zip_longest

lim1=list(zip_longest(lst1,lst2,fillvalue='Not found'))
print("using zip longest function \n",lim1)
















