def split_and_join(line):
    split_list = line.split()
    join_list = "-".join(split_list)
    return join_list

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
