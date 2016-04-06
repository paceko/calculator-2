# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read

def calc():
    """Take input and decide which function to call to evaluate"""
    while not_q:
        input = open('file_name')
        tokens = input.split(" ") #tokenizing the input aka pow 3 5 into [pow, 3, 5]
        
