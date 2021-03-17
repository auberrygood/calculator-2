"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

##User input 
def change_user_input_to_list():
    user_input = input('Enter your equation here: ')
    user_input_list = user_input.split(' ') 
    return (user_input_list)


while True:  
    user_list = change_user_input_to_list()
    if len(user_list) < 3:
        print( "Too short of an equation")
        continue
    elif len(user_list) > 3:
        print ( "Too long of an equation")
        continue
    operator = user_list[0]
    num1 = float(user_list [1])
    num2 = float(user_list [2])
    if operator == 'q':
        print ('Thanks for playing our awesome game!')
        break  
    elif operator == 'add':
        print(add(num1, num2))
            

#            (decide which math function to call based on first token)
#            if the first token is 'pow':
#                  call the power function with the other two tokens

 #           (...etc.)