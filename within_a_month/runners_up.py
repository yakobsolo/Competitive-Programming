if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
temp = 0
j = 0
i = 0

while i < n - 1:
    if arr[i] > arr[i + 1]:
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
    i += 1
while j < n - 2:
    if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
    j += 1

if arr[j] == arr[i]:
    while j >= 0:
        if arr[j] != arr[j - 1]:
            print(arr[j - 1])
            break
    j -= 1
else:
    print(arr[j])
