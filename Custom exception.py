# Exception Handling #

class CustomException(BaseException):
    def __init__(self,msg):
        self.msg=msg
        
try:
    lst=[1,2,3,4,-1]
    for ele in lst:
        if ele<0:
            raise CustomException("The number is negative")

except CustomException as T:
    print(T)
