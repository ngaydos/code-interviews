def string_rotate(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)