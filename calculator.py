"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

##User input 
def change_user_input_to_list():
    user_input = input('Enter your equation here: ')
    user_input_list = user_input.split(' ') 
    return (user_input_list)


#while exit_condition_not_reached:
#    input = consume_input()
#    output = evaluate_input(input)
#    print(output)


#repeat forever:
#    read input
#    tokenize input
#        if the first token is "q":
#            quit
#        else:
#            (decide which math function to call based on first token)
#            if the first token is 'pow':
#                  call the power function with the other two tokens

 #           (...etc.)