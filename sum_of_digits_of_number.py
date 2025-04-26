# Defining the function for sum of the digits
def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10  # by doing eg 123 % 10 the last digit(3) is removed

        # add the 3 to the sum which was 0 but now it will become 3
        # by doing eg. 123 // 10 we still remove the least digit which is 3 and 12 will be left
        # the same operation occurs for the remaining 12 where 12 % 10 the last digit(2) is removed and this is done till there is no digit left
        num = num // 10
    return sum


print(sum_digits(123)) #output is 6

