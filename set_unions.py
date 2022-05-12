n = int(input())
student_english = set(input().split())
b = int(input())
student_french = set(input().split())

total_students = student_english.union(student_french)
print(len(total_students))
