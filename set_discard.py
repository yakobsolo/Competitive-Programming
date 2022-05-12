n = int(input())
s = set(map(int, input().split()))
N = int(input())

for x in range(N):
    string_command = input().split()
    
    for k in range(1, len(string_command)):
        string_command[k] = int(string_command[k])
        
    if string_command[0] == "pop":
        s.pop()
    elif string_command[0] == "remove":
        s.remove(string_command[1])
    elif string_command[0] == "discard":
        s.discard(string_command[1])
summation = 0
for x in s:
    summation += x
print(summation)
