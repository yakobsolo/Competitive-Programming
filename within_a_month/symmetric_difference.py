M = input()
set_one = input().split()
set_one = list(map(int, set_one))
set_one = set(set_one)

N = input()
set_two = input().split()
set_two = list(map(int, set_two))
set_two = set(set_two)
only_set_one = set_one.difference(set_two)
only_set_two = set_two.difference(set_one)
together = only_set_two.union(only_set_one)

sorted_set = sorted(together)
for x in sorted_set:
    print(x)
