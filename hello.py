a=input("Enter a string")
m = list(a)
space = 0
ra = len(a)
for i in range(ra - 1):
    if (m[i] == ' '):
        space += 1
print(f"total number of spaces are : {space}")
print(f"total number of words are : {space + 1}")


