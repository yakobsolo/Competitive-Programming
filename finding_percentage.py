if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    particular_student_values = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    particular_student_values = student_marks.get(query_name)
    total = sum(particular_student_values)
    average = total / len(particular_student_values)

    print("{:.2f}".format(average))
