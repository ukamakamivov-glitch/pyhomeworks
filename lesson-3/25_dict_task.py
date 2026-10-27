# Birinchi key-value juftligini olish. Dictionarydan birinchi key-value juftligini oling.

dic = {
    'c':3,
    'd':2,
    'a':1,

}

ls = list(dic.keys())
ln = list(dic.values())
new = {ls[0] : ln[0]}

print(new)

# yana qisqaroq usuli

fistr = list(dic.items())[0]

print(fistr) #tuple holda chiqish #qandaady holda chiqish haqida suramagan