# Keyni olib tashlash. Dictionary va key berilgan. Agar key mavjud bo‘lsa, uni olib tashlang; mavjud
# bo‘lmasa, shu holatni ham hisobga oling


dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :2
}

n = 'c'

if n in dic:
    del dic[n]
    print(dic)
else:
    print('n key mavjud emas')
