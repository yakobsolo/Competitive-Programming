def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        return leap

    # Write your logic here
    
    return leap

year = int(raw_input())
