from myfunction import *

def call_fun(a,b,fun_name):
    if fun_name=='sum':
        result=sum(a,b)
        print("The addition of two number is- ",result)
    elif fun_name=='diff':
        result=diff(a,b)
        print("The subtraction of two number is- ",result)
    elif fun_name=='mul':
        result=mul(a,b)
        print("The multiplication of two number is- ",result)
    else:
        result=div(a,b)
        print("The divison of two number is- ",result)


call_fun(4,5,'div')
        
        
