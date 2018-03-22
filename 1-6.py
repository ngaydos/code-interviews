#Implement a method to perform basic string compression, using the counts of repeated characters.
#Example: aabcccccaaa becomes a2b1c5a3
#if the compressed string is not any smaller, return the original string

def string_compression(string):
    '''compresses a string as defined previously
    input: string
    ouput: string'''

    #sets up initial variables and blank final string
    counting_char = string[0]
    count = 0
    final_string = ''
    for char in string:
        #increases the current count if the character matches
        if char == counting_char:
            count += 1
        #if the character does not match, adds the  working character and the count to the final string and starts over with new string
        else:
            final_string += (counting_char + str(count))
            count = 1
            counting_char = char
    #adds the last set of number and count to the final string
    final_string += (counting_char + str(count))
    #checks the compared length to determine what should be returned
    if len(final_string) < len(string):
        return final_string
    else:
        return string