if __name__ == '__main__':
    n = int(input())
    student_name_score = []
    student_score = []
    for i in range(n):
        
        name = input()
        score = float(input())
        student_name_score.append([name, score])
        student_score.append(score)
        
    sorted_score = sorted(set(student_score))
    second_min_score = sorted_score[1]
    second_min_names = []
    for j in student_name_score:
        if second_min_score == j[1]:
            second_min_names.append(j[0])
    
    
    second_min_names = sorted(second_min_names)
    for k in second_min_names:
        print(k
