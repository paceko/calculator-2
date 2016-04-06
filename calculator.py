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
        input = raw_input("Please give me a prefix expression. ")
        token = input.split(" ") #tokenizing the input aka pow 3 5 into [pow, 3, 5]
        # print token, testing to see what our tokens looked like
        if token[0] == 'q':
            return None
        elif token[0] == '+':
            return token[1] + token[2]
        elif token[0] == '-':
            return token[1] - token[2]
        elif token[0] == '*':
            return token[1] * token[2]
        elif token[0] == '/':
            return float(token[1]) / token[2] 
        elif token[0] == 'square':
            return token[1] ** 2
        elif token[0] == 'cube':
            return token[1]** 3
        elif token[0] == 'pow':
            return token[1] ** token[2]
        elif token[0] == 'mod':
            return token[1] % token[2]
        else: 
            print 'That was not the correct prefix expression!'

calc()