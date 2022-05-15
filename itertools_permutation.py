from itertools import permutations
input_string, input_int = input().split()
input_int = int(input_int)
input_string = sorted(input_string)
output = permutations(input_string, input_int)
for x in output:
    print(*x, sep = '')
