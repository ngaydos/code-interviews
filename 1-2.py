#Question 1.2 - given two strings, write a method to determine if one is a permutation of the other.

def check_permutations(string1, string2):
    '''
    determines if two strings contain the exact same characters
    input: two strings
    output: boolean
    '''
    l1 = list(string1)
    l2 = list(string2)
    sorted1 = l1.sort()
    sorted2 = l2.sort()
    if sorted1 = sorted2:
        return True
    else:
        return False