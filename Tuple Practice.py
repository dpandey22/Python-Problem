#============ Tuple Practial=================

# Tuple is ordered and imutable -:
# after declaring tuple, addition and deletion can not be performed.
tup=(4,5,6,9,2,8)
print(tup)
print(type(tup))

# slicing of tuple--
# we can slice tuple same as list
print(tup[2]) # single element

# multiple element

print(tup[2:5]) # multiple element

# negative slicing

print(tup[-5:-1]) # negative slicing

# mixed slicing

print(tup[-5:3]) # mixed slicing

############# Accesing tuple element through loop ##############
# this is the first way to access tuple element

for ele in tup:
    print(ele)

print("==================")
# accesing tuple element through range and len function
for ele in range(len(tup)):
    print(tup[ele])
    

############### Tuple functions #########################
#min,max,count,index,len,sum

print("minimum value of tuple-:",min(tup))
print("maximum value of tuple-:",max(tup))

# count element occurance

print(tup.count(6))

# length of the tuple-:
print(len(tup))

# to know the index position of specific number

print(tup.index(6))

## to know the total of tuple, but for this tuple should be consist numeric value

print("total of tuple-",sum(tup))




############### # Printing table 2 to 4 ##############
start=2
end=4
for num in range(start,end+1):
    for n in range(1,11):
        print(f"{num}X{n}={num*n}")
    print("===============")













