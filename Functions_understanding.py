def print_val(a):
    
    print("The value is -:", a)

print_val(10)


## with return statement

def return_val(b):
    return b

#print(return_val(25))
val=return_val(25)
print("The value is returned-:",val)


### understnding the local and global variable
# local variable can not be used inside the function.
# if you want to use local variable value inside the function the need to use
# global keyword inside the functions

##-------- local variable use case------

def fun(a):
    a=65 # this is function local variable
    print("inside the function-:",a)

a=25 # this value can not be reffered inside the function
fun(10)
print("outside the function-:",a)

### use case of global variable ===========

def withdraw(amount):
    global account_balance # this will throw an error because of local variable, need to use gloable keyword

    account_balance=account_balance-amount
    print("balance amount is-",account_balance)

account_balance=10000
withdraw(2000)
print("outside the function-:",account_balance)
    
##### positional argument and keyword argument------
def print_name(fname,lname,mname=''): # making mname is optional
    print(fname,mname,lname)

# with position----
print_name('Dinesh','Pandey')

# with keyword----

print_name(lname='Pandey',fname='Dinesh',mname='Kumar')

# to handle variable length use * (tuple), **(dictionary)

#variable length of postional argument
def tup(*a):
    print(a)

tup(1,2,3,6)

# variable positional length

def var_pos(**a):
    print(a)

var_pos(a=1,b=5,c=52)










