# Defining the function
def loop_factorial(x):
    """
    # initializing the result to 1 to ensure the multiplication is well done because
    when a number is multiplied by 1 it gives the same number rather than 0 which
    undermines the process of multiplication
     """
    result = 1
    for y in range(1, x + 1):  # range generates a sequence of numbers in this case from 1 to x
        result *= y  # Multiplication
    return result


# calling the function
print(loop_factorial(4)) #output is 24