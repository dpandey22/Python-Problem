def list_gen():
    for i in range(1000):
        if i%13==0:
            yield i

result=list_gen()
'''
11. What is the use of key parameter in sorted function? Sort the below list by the length of each 
    string in descending order. lst = ["Ramadas","Sam","Li","Tina","Priyanka"]
'''
lst = ["Ramadas","Sam","Li","Tina","Priyanka"]
print(sorted(lst,key=lambda x: len(x)))


