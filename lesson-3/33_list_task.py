##Barcha indexlarni topish. List va element berilgan. Shu element uchraydigan barcha indexlarni
#toping.


ls = [1,4,2,23,6,12,6,1,4,23,3]

n = 4
index =[]
# print(ls.index(n))
# m  = ls.index(n)
# ls.pop(m)
# print(ls.index(n)+1)

for x in range(len(ls)):
    if ls[x] == n:
        index.append(x)

print(index)
