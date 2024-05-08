# count the character in a string:-,

string='Google.com'

dict1={}

for ele in string:
    if ele not in dict1.keys():
        dict1[ele]=1
    else:
        dict1[ele]=dict1.get(ele)+1

print(dict1)

'''
 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2,
return the empty string instead.
'''
# Solution-:

string1='w3resource'
if len(string1)>=2:
    output_str=string1[:2]+string1[-2:]
else:
    output_str=''
#print(output_str)

## same solution with function-:
def comp(a):
    if len(a)>=2:
        return a[:2]+a[-2:]
    else:
        return ''

output=comp('w3resource')
print(output)


'''
4. Write a Python program to get a string from a given string where all occurrences of its first char
have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

'''

string3='restart'
str1=''
for ele in string3:
    if (ele==string3[0]) and (ele in str1):
        str1=str1+'$'
    else:
        str1=str1+ele
print(str1)

### another way

string3='restart'
char=string3[0]
string3=string3.replace(char,'$')
string3=char+string3[1:]
print(string3)


'''

5. Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

'''
string4='abc'
string5='xyz'

new_str=string5[:2]+string4[2:] +' '+ string4[:2]+string5[2:]
print(new_str)


