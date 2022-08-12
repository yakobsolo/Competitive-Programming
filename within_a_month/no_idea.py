# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr_a = set(map(int, input().split()))
arr_b = set(map(int, input().split()))

happiness = 0
for x in arr:
    if x in arr_a:
        happiness += 1
    elif x in arr_b:
        happiness -=1
    else:
        pass
print(happiness)
        
