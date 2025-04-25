#Definition of the function
def sum_number(num):
 sum=0                #At this point the sum should be initialized to 0 for accurate addition
 for number in num :   #The for loop enables iteration that will help perform addition
   sum+=number           #This enables us to add the numbers to the current sum
 return sum  #it returns the sum of the elements

num=[1,2,3,4,5,6,7,8,9]
print(sum_number(num))  #calls the function