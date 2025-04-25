# Defining function
def factorial_recursion(x):
    if x == 0:  # At this point the return is 1 as 0!=1
        return 1
    else:
        return x * factorial_recursion(x - 1)  # the function is calling itself


print(factorial_recursion(4))  # output will be 24