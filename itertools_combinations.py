from itertools import combinations

input_string, input_int = input().split()
input_int = int(input_int)

sorted_string = sorted(input_string)
for x in range(1, input_int + 1):
    for i in list(combinations(sorted_string, x)):
        print(*i, sep = "")
