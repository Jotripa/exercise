#input student's heights
student_heights = input("Input the heights: ").split()
for x in range (0, len(student_heights)):
    student_heights[x] = int(student_heights[x])
#calculating
total_heights = 0
for height in student_heights:
    total_heights += height
print("The total of heights are : " + str(total_heights))

number_students = 0
for student in student_heights:
    number_students += 1
print("The total of students are : " + str(number_students))

average = round(total_heights / number_students)
print("The average heights of the students are : " + str(average))