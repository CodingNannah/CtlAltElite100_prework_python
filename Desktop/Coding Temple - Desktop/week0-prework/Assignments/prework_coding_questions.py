# Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of code has been defined as below:
print(' ')
print('Answer to Question 1:')

def hello_name(user_name):
    username_cap = user_name.upper() # to make name ALL CAPS
    print("Hello, " + username_cap + "!")
#input:
hello_name("mr. president") # passing in the name

print(' ')

# making the name caps the way it should be:
print('Answer to Question 1 (part2):')
def hello_name(user_name):
    username_c = user_name.title() # to make name first letter CAPS
    print("Hello, " + username_c + "!")
#inputs:
hello_name('diana')
hello_name('coding nannah')

print(' ')

# Question 2: Write a function, first_odds that prints the odd numbers from 1-100 and returns nothing
print('Answer to Question 2:')
def first_odds():
    for num in range (1, 101, 2):
        print(num)
#input:
first_odds() # returns nothing, unless called, as here

print(' ')

# Question 3: Write a function, max_num_in_list to return the max number of a given list. The first line is defined.
print('Answer to Question 3:')
def max_num_in_list(a_list):

    max = a_list[0] # start from beginning of a list
    for num in a_list:
        if num > max:
            max = num # this will rewrite the max number as the number to compare with next:
    return max # not print! use return - check indent 
    # print(max) # to see it & test if it's working!
#input:
print(max_num_in_list([1, 7, 12, 5, 365, 14, 6, 18])) #passing in the list

print(' ')

# Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4 but not by 100, unless it is also divisible by 400. (IF ELIF ELSE!) The return should be boolean Type (True/False).
print('Answer to Question 4:')
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
#   elif year % 400 == 0:
#         return True   
        # this is unnecessary: div by 4 covers dif by 400!
    else:
        return False
        
#inputs:
print(is_leap_year(1998))
print(is_leap_year(2000))
print(is_leap_year(2020))
print(is_leap_year(2222))
print(is_leap_year(2028))

print(' ')

# Question 5: # Write a function to see if all numbers in a list are consecutive. The return should be boolean Type (True/False).# Hint: Associative property of addition. If a number is equal to the next number, then...
print('Answer to Question 5:')
def is_consecutive(a_list):
    for i in range(len(a_list)-1): # i = integer; want the length of the enitire list
        if a_list[i] + 1 == a_list[i+1]:
            return True  
        else:
            return False
        
print(is_consecutive([1,2,3,4,5,6,7]))
print(is_consecutive([3,6,9,12,15,18]))
print(is_consecutive([12,0,4,27,6,2]))
print(is_consecutive([48,49,50,51]))