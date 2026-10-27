# Listni aylantirish. List berilgan. Elementlari o‘ngga surilgan, ya’ni aylantirilgan yangi list yarating.

ls = [1,4,2,23,6,12,6,1,4,23,3]
#right rotation
lm = ls[-1:] + ls[:-1]
#print(ls[-1:])
#print(ls[:-1])
print(lm)