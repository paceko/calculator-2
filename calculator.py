from arithmetic import *

# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read

def calc():
    """Take input and decide which function to call to evaluate"""
    while True:
        print 'welcome to the calculator!'
        prefix = raw_input("Please give me a prefix expression. ")
        token = prefix.split(" ") #tokenizing the input aka pow 3 5 into [pow, 3, 5]
        
        if token[0] == 'q':
            return

        elif token[0] == '+':
            print add(int(token[1]), int(token[2])) #add(int(num1), int(num2))

        elif token[0] == '-':
            print subtract(int(token[1]), int(token[2]))

        elif token[0] == '*':
            print multiply(int(token[1]), int(token[2]))

        elif token[0] == '/':
            print divide(int(token[1]), int(token[2])) 

        elif token[0] == 'square':
            print square(int(token[1]))

        elif token[0] == 'cube':
            print cube(int(token[1]))

        elif token[0] == 'power':
            print power(int(token[1]), int(token[2]))

        elif token[0] == 'mod':
            print mod(int(token[1]), int(token[2]))

        else: 
            print 'That was not the correct prefix expression!'

calc()