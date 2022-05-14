# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

C = list(product(A, B))
print(*C)
