#Implement a method to perform basic string compression, using the counts of repeated characters.
#Example: aabcccccaaa becomes a2b1c5a3
#if the compressed string is not any smaller, return the original string

def string_compression(string):
    '''compresses a string as defined previously
    input: string
    ouput: string'''
    counting_char = string[0]
    count = 0
    final_string = ''
    for char in string:
        if char == counting_char:
            count += 1
        else:
            final_string += (counting_char + str(count))
            count = 1
            counting_char = char
    final_string += (counting_char + str(count))
    if len(final_string) < len(string):
        return final_string
    else:
        return string