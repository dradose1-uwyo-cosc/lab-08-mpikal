# Matthew Pikal
# UWYO COSC 1010
# Submission Date: 11/5/2024
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# I thought it would be better to not require the 
# user to say exit when they have already given all the information needed in the while loops

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def check_str(var):
    if var.isdigit():
        return int(var)
    else:
        try:
             float(var)
             return float(var)
        except:
            return False



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m, b, lower, upper):
    x = 0
    if int(upper) < int(lower) or check_str(m) == False or check_str(b) == False or lower.isdigit() == False or upper.isdigit() == False:
        return print('Error')
    else: 
        m = check_str(m)
        b = check_str(b)
        upper_bound = int(upper)+1
        lower_bound = int(lower)
        list = []
        for x in range(lower_bound, upper_bound):
            y = (m*x)+b
            list.append(y)
        return list
i = 0
while i<4: ## I thought it would be better to not require the the user to say exit when they have already given all the information needed
    slope = input('Please enter a slope')
    i+=1
    intercept = input('Please enter your y intercept')
    i+=1
    lower = input('Please enter a lower bound')
    i+=1
    upper = input('Please enter an upper bound')
    i+=1
print(slope_intercept(slope, intercept, lower, upper))



            


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quad(a, b, c):
    a = check_str(a)
    b = check_str(b)
    c = check_str(c)
    try: 
        y = (b*(-1))+(((b**2)-(4*a*c))**(1/2))/(2*a)
        x = (b*(-1))-(((b**2)-(4*a*c))**(1/2))/(2*a)
        return y,x
    except:
        return 'No real roots'
index = 0
while index<3:
    a = input('Please enter the A from your equation when in the from y = A(x^2)+Bx+C')
    index+=1
    b = input('Please enter the B from your equation when in the from y = A(x^2)+Bx+C')
    index+=1
    c = input('Please enter the C from your equation when in the from y = A(x^2)+Bx+C')
    index+=1
print(quad(a, b, c))
def root(num):
    if str(num)[0] == '-':
        return 'null'
    else:
        return int(num)**(1/2)