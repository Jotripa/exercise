#input scores
student_scores = input("Input the students score : ").split()
for x in range(0, len(student_scores)):
    student_scores[x] = int(student_scores[x])
print(student_scores)
#calculating
highest_scr = 0 
for score in student_scores:
    if score > highest_scr:
        highest_scr = score
print(f"The highest score is : {highest_scr}")