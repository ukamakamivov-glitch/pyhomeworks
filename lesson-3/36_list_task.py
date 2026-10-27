# Musbat sonlar yig‘indisi. Sonlardan iborat list berilgan. Barcha musbat sonlarning yig‘indisini
# hisoblang.

ls = [1,2,3,-7,4,5,-2]

m = len(ls)
suma = []
for i in range(m):
    if ls[i] > 0:
        suma.append(ls[i])


print(sum(suma))