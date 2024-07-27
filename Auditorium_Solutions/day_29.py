list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:


# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = []
for num in list_of_strings:
    if int(num) % 2 == 0:
        result.append(int(num))

# Write your code 👆 above:
print(result)