list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]



list3 = list1 + list2
result = []

for i in list1:
    if i not in list2:
        result.append(i)
for i in list2:
    if i not in list1:
        result.append(i)

print(result)