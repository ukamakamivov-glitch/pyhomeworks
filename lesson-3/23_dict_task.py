# Umumiy keylarni tekshirish. Ikkita dictionary berilgan. Ularda umumiy keylar bor yoki yo‘qligini
# tekshiring.


dic = {
    'c':3,
    'd':2,
    'a':1,

}

dic2 = {
    'e':3,
    'p':2,
    'c':1,

}

a = dic.keys()
b = dic2.keys()
c =0
for i in a:
    if i in b:
        c = c + 1
        break
if c >0 :
    print("true")
else:
    print("false")

    # 2   -  usul

print(bool(dic.keys() & dic2.keys()))