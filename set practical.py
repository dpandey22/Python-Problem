#======== Sets in python================

st={10,20,30,45}
print(st)

#It is collecion of unordered and unindexed
# sets functions are :-
# add,set,clear,pop, remove,update,discard

# adding element to set

st.add(50)
print("after adding element-:",st)

# to delete any random element from set
print("deleting random number",st.pop())

# to delete a specific number
st.remove(20)
print("after removing 20 ",st)

# adding multiple element to set
st.update([40,25,40,35])
print("after updating set",st)

# discard element from set
st.discard(40)
print("after dicard 40",st)

# what is differene between discard and remove-
# remove will throgh error if element is not present while discard will not.

#st.remove(101)  # it will give error
st.discard(101) # it will not give error.....

#Qns- how to remove duplicate value from the list
lst=[10,45,60,10,20,30,20]
print("Actual list-:",lst)
st=set(lst)
print("after removing duplicate-: ",list(st))


### slicing is not possible in set
#print(st[0]) # it will through error because set is unordered

# accessing set element-:

for ele in st:
    print(ele)












