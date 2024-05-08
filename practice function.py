def sum_product(*a):
    #print(a)
    sum_value=sum(a)
    #print(product(a)) # product method is available for tuple
    product_mul=1
    for ele in a:
        
        product_mul=product_mul*ele
    return sum_value,product_mul

abc,dec=sum_product(4,5,6,8)
print(f"The sum of the value is-{abc} and product is- {dec}")
print("The sum of the value is-{} and product is- {}",abc,dec)
