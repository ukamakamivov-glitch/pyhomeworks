# Ichma-ich tuple yaratish. Asl tupledan ko‘rsatilgan elementlarni o‘z ichiga oluvchi subtuplelardan
# tashkil topgan yangi tuple yarating.


tp = ('a', 'b', 'c', 3, 1, 0, 3, 'a')

n = len(tp) // 2

tp_new = (tp[:n], tp[n:])

print(tp_new)