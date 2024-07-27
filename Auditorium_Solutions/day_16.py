# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_count = 0;
total_height = 0;
for height in student_heights:
    total_count += 1
    total_height += height

average_height = total_height / total_count
int_average_height = int(average_height)
decimal_part = average_height - int_average_height
if decimal_part > 0.5:
    int_average_height += 1

print("total height =", total_height)
print("number of students =", total_count)
print("average height =", int_average_height)