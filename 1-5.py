#an edit is either removing one character, adding one character or replacing one character.
#write a function to determine if two strings are 1 (or 0) edits apart.

def one_edit(string1, string2):
    #if two strings are duplicate return True
    if string1 == string2:
        return True
    #if two strings are the same length checks if they can be modified with a single edit
    if len(string1) == len(string2):
        #creates a bool to check if a single character doesn't match
        different_char = False
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                if different_char == False:
                    different_char = True
                else:
                    return False
        return True

    if len(string1) > len(string2):
        for i in range(len(string2)):
            if string1[i] != string2[i]:
                new_string = string1[:i] + string1[(i+1):]
                if new_string == string2:
                    return True
                else:
                    return False
        return True
                
    if len(string2) > len(string1):
        for i in range(len(string1)):
            if string2[i] != string1[i]:
                new_string = string2[:i] + string2[(i+1):]
                if new_string == string1:
                    return True
                else:
                    return False
        return True