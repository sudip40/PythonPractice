# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_number = 0

for number in student_scores:
    if highest_number < number:
        highest_number = number

print("The highest score in the class is:", highest_number)