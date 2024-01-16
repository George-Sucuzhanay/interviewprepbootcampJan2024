# longest repeating character replacement

def characterReplacement(s, k):
    l, max_length = 0, 0
    repeated_string = ""
    k_counter = k
    
    for r in range(len(s)):
        if s[r] in repeated_string: # moves l
            repeated_string += s[r]
            max_length += 1
        else:
            if repeated_string == "":
                repeated_string += s[r]
                max_length += 1
                r += 1
            elif k_counter != 0:
                repeated_string += repeated_string[:-1]
                max_length += 1
                r += 1
                k_counter -= 1
            else:
                continue
    return max_length


# def classExampleCharacterReplacement(s,k):
#     char_count = {}
#     l, max_length = 0, 0
#     for r in range(len(s)):
#         if 

    