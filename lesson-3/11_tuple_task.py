#  Elementning barcha indexlarini olish. Tuple va element berilgan. Shu element uchraydigan barcha
# indexlarni toping.

tp = (3,2,5,4,5,2,0)
n = 5
ls = []
for i in range(len(tp)):
    if tp[i] == n:
        ls.append(i)

print("Barcha indexlar : ",tuple(ls))