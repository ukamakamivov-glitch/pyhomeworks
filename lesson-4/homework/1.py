list1 = [1, 1, 2]
list2 = [2, 3, 4]

# output : [1,1,3,4]

list3 = list1 + list2
result = []

for i in list1:
    if i not in list2:
        result.append(i)
for i in list2:
    if i not in list1:
        result.append(i)

print(result)