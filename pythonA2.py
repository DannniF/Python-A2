print("Hello from inside a File!")

# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    x = max(a,b,c)
    print(x)

max_num(6,5,2)

# Write a Python function called mult_list() to multiply all the numbers in a list.
numbers = [3,4,5,6,3,4,6,78,8,9,7,6]
def mult_list(numbers):
    b = sum(numbers)
    print(b)

mult_list(numbers)

# Write a Python function called rev_string() to reverse a string.
#resusing numbers on line 11 
def rev_string(numbers):
    x = numbers [::-1]
    print(x)

rev_string(numbers)
'''
Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

'''
def num_within(number, min, max):
    if number > min and number < max:
        return True
    else:
        return False
    
print(num_within(20,1,24))
'''
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
'''
#notes: breakdown of the code: so for i in range we are setting a start and stop so.
# we are then printing spaces and end= is a new line 
# maknig c equal to 1 makes our first number in the row a one , so then we print 1 
# sep= adds what ever you want between arguments
# then we have an equation which creates our pyramid 

def pascal(n):
 for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
    C = 1
    for j in range(1, i+1):
        print(' ', C, sep='', end='')
        C = C * (i - j) // j
    print()
    

pascal(3)
pascal(5)