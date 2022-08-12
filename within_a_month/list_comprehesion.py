if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

my_list = [[ex,ey,ez] for ex in range(x + 1) for ey in range(y + 1) for ez in range(z + 1) if ex + ey + ez != n]
print(my_list)
