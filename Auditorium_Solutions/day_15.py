line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
col = 0
if position[0] == "A":
    col = 0
elif position[0] == "B":
    col = 1
else:
    col = 2

row = int(position[1]) - 1

selected_row = line1
if row == 0:
    selected_row = line1
elif row == 1:
    selected_row = line2
else:
    selected_row = line3

selected_row[col] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
