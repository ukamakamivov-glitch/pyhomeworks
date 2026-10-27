# Default dictionary yaratish. Mavjud bo‘lmagan keylar uchun default value taqdim etadigan
# dictionary yarating.

from collections import defaultdict


dic = defaultdict(int)


dic['a'] = 2
dic['b'] = 3


print(dic['c'])

print(dic)