student_marks_string = input("Input a list of student heights: ").split(" ")
student_marks = [int(x) for x in student_marks_string]

maximum = 0
for mark in student_marks:
    if mark > maximum:
        maximum = mark

print(maximum)