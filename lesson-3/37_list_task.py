# 37. Manfiy sonlar yig‘indisi. Sonlardan iborat list berilgan. Barcha manfiy sonlarning yig‘indisini
# hisoblang.

ls = [1,2,3,-7,4,5,-2]

lm = []
for x in range(len(ls)):
    if ls[x] < 0:
        lm.append(ls[x])

print(sum(lm))

