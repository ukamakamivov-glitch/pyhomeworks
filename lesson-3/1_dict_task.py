# Value olish. Dictionary va key berilgan. Shu keyga tegishli valueni oling.
# Agar key mavjud bo‘lmasa,
# nima qaytarishni ham hisobga oling.

dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :2
}
key = 'b'
if key in dic.keys():
    print(dic[key])
else:
     print("bunday key mavjud emas")