#Question 1.3 - Write a method to separate all spaces in a string with '%20'.

def URLify(string):
    '''replaces all cases of a space with %20 without using replace function
    input: string
    output: string'''
    acc = ''
    for char in string:
        if char == ' ':
            acc += '%20'
        else:
            acc += char
    return acc