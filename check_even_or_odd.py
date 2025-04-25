# Defining the function
def check_even_odd(num):
    if num % 2 == 0:  # Checking if the number is even
        return "Even Number"  #output if the number is even
    else:
        return "Odd Number" # output when the number is not even


Num = int(input("Enter the number: "))  # Input the number for checking
print(check_even_odd(Num))  # calling the function

