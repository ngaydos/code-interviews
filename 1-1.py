#Question 1.1 - implement an alogirithim to determine if a string has all unique characters.

def is_unique(string):
    '''
    input: string
    output: bool
    '''
    acc = []
    for letter in string:
        if letter in acc:
            return False
        else:
            acc.append(letter)
    return True

#what if you cannot use additional data structures?

def is_unique(string):
    '''
    input: string
    output: bool
    '''
    #iterates through each letter in the string and checks the following characters of the string to ensure they are unique
    for value in range(len(string)-1):
       if string[value] in string[value+1:]:
        return False
    return True