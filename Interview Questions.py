# Calculate the factorial

'''
def fact1(num):
    result=1
    for i in range(num,0,-1):
        result=result*i
    return result

output=fact1(6)
print(output)

'''

# recursive function
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(6))
'''
# check palindrome or not-:
'''
def palindrome(string):
    if isinstance(string,int):
       string=str(string)
        
    else:
        pass
    
    if string==string[::-1]:
        return "It is palindrome"
    else:
        return "It is not palindrome"

print(palindrome('Navin'))
'''

'''
num=121
print(isinstance(num,int))
print(str(num)[0:1])
'''

# count of vowel-:
'''
def count_of_vowel(string):
    vowel=['a','e','i','o','u','A','E','I','O','U']
    cnt=[]
    for ele in string:
        if ele in vowel and ele not in cnt:
            cnt.append(ele)
    return len(cnt)

print(count_of_vowel('Knwoledge'))
'''
# find largest value in a list of integer
'''
with using max function

lst=[1,2,3,5]
print(max(lst))
'''
'''
without using max function

def largest_num(lst):
    lrg=0
    for ele in lst:
        if ele>lrg:
            lrg=ele
        else:
            lrg=lrg
    return lrg
print(largest_num([1,10,3,5]))
'''

## reverse a string with function & without function
'''
def rev_str(string):
    print("with in-built function",''.join(reversed(string)))
    print("without using in-built function",string[::-1])

rev_str('vinay')
'''

# check number is prime or not:-
'''
def check_prim(num):
    msg=''
    if num>0:
        if num==1:
            msg='prime_number'
        else:
            for ele in range(2,num+1):
                if num%ele==0:
                    if num==ele:
                        msg='prime_number'
                    else:
                        msg='not prime number'
                        break
    return msg

print(check_prim(11))
'''
'''
def check_prime(num):
    flag=False
    if num>0:
        for ele in range(2,num):
            if num%ele==0:
                flag=True
                break
    if flag:
        print("it is not prime no")
    else:
        print("it is prime no")


check_prime(11)
'''

# find out the mdian of list of integer:

def median_1(lst):
    cnt=len(lst)
    lst.sort()
    if cnt%2==0:
        m1=lst[cnt//2]
        m2=lst[cnt//2-1]
        m=(m1+m2)/2
        return m
    else:
        return lst[cnt//2]

print(median_1([1,2,3,4,5,6]))


















