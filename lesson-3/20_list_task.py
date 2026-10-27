# Ikkinchi eng katta element. Berilgan listdagi ikkinchi eng katta elementni toping.

ls = [1,4,2,23,6,12,6,6,4,23]

mx = max(ls)

ls = list(filter(lambda x : x != mx, ls))

m2 = max(ls)

print("ikkinchi kattason : ", m2)

