"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)

from functools import reduce
#import ascii

##User input 
command_list = ['add', 'subtract', 'multiply', 'divide', 'square', 'cube',
                        'power', 'mod', 'add_mult', 'add_cubes']

def change_user_input_to_list(command_list):
   while True:      
        user_input = input('Enter your equation here: ')
        user_input_list = user_input.split(' ') 
        operator = user_input_list[0]
        num1 = user_input_list [1]
        if 'q' in user_input_list:
            print ("Thanks for playing this awesome game")
            break 
        if user_input_list[0] not in command_list: 
            print ('Please enter valid command') 
            continue  
        if len (user_input_list) < 2: 
            print ('Not enough input')
            continue
        elif len (user_input_list) < 3: 
            num2 = '0'
        else: 
            num2 = user_input_list[2]
        
        elif len (user_input_list) < 4:
            num3 = '0' 
        else: 
            num3 = user_input_list[3]

        if not num1.isdigit() or not num2.isdigit():
            print("Those aren't numbers!")
            continue
        
        return [operator, num1, num2, num3]


user_input_from_func =  change_user_input_to_list(command_list)
print (user_input_from_func)


def arithmetic_stuff (user_input_from_func): 

    operator = user_input_from_func[0]
    num1 = float(user_input_from_func[1])
    num2 = float(user_input_from_func[2])
    num3 = float(user_input_from_func[3])

    if operator == 'add':
        print(add(num1, num2))
    elif operator == 'subtract':
        print (subtract(num1, num2))
    elif operator == 'multiply':
        print (multiply(num1, num2))
    elif operator == 'divide':
        print (divide(num1, num2))
    elif operator == 'square':
        print (square(num1))
    elif operator == 'cube':
        print (cube(num1))
    elif operator == 'power':
        print (power(num1, num2))
    elif operator == 'mod':
        print (mod(num1, num2))
        
    '''our add_mult and add_cubes are not working, program returns error of 'add_mult' is not defined'''
    # elif operator == 'add_mult':
    #    print (add_mult(num1, num2, num3))
    # elif operator == 'add_cubes':
    #    print (add_cubes(num1, num2))

arithmetic_stuff(user_input_from_func)

