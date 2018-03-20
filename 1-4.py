#given a string write a function to check if it is a permutation of a palindrome

def palindrome_check(string):
    '''checks if a string can be made into a palindrome
    input: string
    output: bool'''
    #creates an empty dictionary
    acc = {}
    #loops over each character in the string, creating a dictionary of counts for each occurence of a character
    for char in string:
        #instructions seemed to indicate to ignore spaces so this passes by all spaces
        if char == ' ':
            continue
        elif char in acc:
            acc[char] += 1
        else:
            acc[char] = 1
    #creates a dummy boolean
    bool_check = False
    #checks if the number of times a letter occurs is odd and if it occurs more than once, returns false
    for val in acc.values():
        if val % 2 != 0:
            if bool_check == False:
                bool_check = True
            else:
                return False
    return True