def count_substring(string, sub_string):
    count = 0
    i = -1
    while i < len(string):
        var = string.find(sub_string,i + 1)
        if var == -1:
            break
        count += 1
        i = var
        
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
