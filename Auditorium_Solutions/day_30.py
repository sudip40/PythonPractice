# Open the file in read mode
with open('file1.txt', 'r') as file:
    content = file.read()
    list1 = content.split()

with open('file2.txt', 'r') as file:
    content = file.read()
    list2 = content.split()

result = []
for num in list1:
    if list2.__contains__(num):
        result.append(int(num))

# Write your code above 👆
print(result)
