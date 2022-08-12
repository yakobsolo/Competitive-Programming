def swap_case(s):
   
    updated_string = ""
    for i in range(len(s)):
        if s[i].isupper():
            updated_string += s[i].lower()
        elif s[i].islower():
            updated_string += s[i].upper()
        else:
            updated_string += s[i]

        
    return updated_string

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
