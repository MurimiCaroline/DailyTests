#function that returns square of parameters
def Mul(a, b):
    return a * b
    
#function that returns the square of the product of the parameters,
def square_of_product(x, y):
    product = Mul(x, y)
    return product ** 2

print (Mul(6,2))
print (square_of_product(6,2))