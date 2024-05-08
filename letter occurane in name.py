# print the occurance of letter in your name through Dictionary

n_str=input("please enter the name-:")
n_str=n_str.replace(" ","")
d={}
for ch in n_str:
    if ch not in d.keys():
        d[ch]=1
    else:
        d[ch]=d.get(ch)+1
print(d)

"""
str_name="Dinesh Kumar"
print(str_name.replace(" ",""))
"""
