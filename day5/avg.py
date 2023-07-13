student_heights_string = input("Input a list of student heights: ").split(" ")
student_heights = [int(x) for x in student_heights_string]

sum = 0
number_students = 0
for height in student_heights:
    number_students += 1
    sum += height

print(round(sum / number_students))