# taking input for multiple variable-:
'''
id,name,salary=input("Enter the value for id,name,salary-: ").split()
print("The ID is-:",id)
print("The Name is-:",name)
print("The salary is-:", salary)
'''

# Solution ####
# running total of a list-:
lst=list(input("enter tha value for the list"))
running_sum=[]
sum=0
for ele in lst:
    sum=sum+int(ele)
    running_sum.append(sum)

print(running_sum)
