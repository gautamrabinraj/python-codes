even_number=list(range(1,101,1))
l=[]

for i in even_number:
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        l.append(i)
print(l)




