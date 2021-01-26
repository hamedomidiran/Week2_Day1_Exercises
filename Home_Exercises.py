# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:22:29 2021

@author: tommywha
"""

"""Exercise 1"""

def calculator(a,b):
    print('The following calculations are available for you to perform \n\n'
          '- addition of a and b \n'
          '- subtraction of a from b \n'
          '- subtraction of b from a \n'
          '- division of a by b \n'
          '- division of b by a \n'
          '- multiplication of a and b \n'
          '- a to the power of b \n'
          '- b to the power of a \n')
    
    Done =    "No"
    
    while Done == "No" or Done == "no":
        calculation = input("What calculation would you like to perform?     ")
        
        if calculation.lower()   == 'addition of a and b':
            print(a+b)
        elif calculation.lower() == 'subtraction of a from b':
            print(b-a)
        elif calculation.lower() == 'subtraction of b from a':
            print(a-b)
        elif calculation.lower() == 'division of a by b':
            print(a/b)
        elif calculation.lower() == 'division of b by a':
            print(b/a)
        elif calculation.lower() == 'multiplication of a and b':
            print(a*b)
        elif calculation.lower() == 'a to the power of b':
            print(a**b)
        elif calculation.lower() == 'b to the power of a':
            print(b**a)
        else:
            print ('\n That calculation is not in our directory')
            
            
        Done = input("Are you done with your calculations?     ")
        
#calculator(20,5)
        

"""Exercise 2"""
def pyramid(n):
    num_of_levels = n
    
    for num in range(n):
        if num != 0:
            left_space = num_of_levels-(num)
            print((left_space*' ')+("X "*num))
    
    print("X "* (n))
    
#pyramid(20)
    
    