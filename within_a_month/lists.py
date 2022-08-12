if __name__ == '__main__':
    N = int(input())
    input_list = []
    
    for i in range(N):
        string = input().split()
        for k in range(1,len(string)):
            string[k] = int(string[k])
            
        if string[0] == "insert":
            input_list.insert(string[1], string[2])
        elif string[0] == "append":
            input_list.append(string[1])
        elif string[0] == "pop":
            input_list.pop()
        elif string[0] == "remove":
            input_list.remove(string[1])
        elif string[0] == "reverse":
            input_list.reverse()
        elif string[0] == "sort":
            input_list.sort()
        elif string[0] == "print":
            print(input_list)
