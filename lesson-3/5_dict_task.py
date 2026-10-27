# Dictionarylarni birlashtirish. Ikkita dictionary berilgan. Ikkalasini birlashtiradigan yangi dictionary
# yarating.
 ##  Barcha valuelarni olish. Dictionarydagi barcha valuelarni o‘z ichiga olgan list yarating.

dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :2
}

dic2 = {
    'a':2,
    'f':'salom',
    'r':4,
     4 :2
}
ls = dic.values()
print(list(ls))
new_dic = dic | dic2
print(list(new_dic.keys()))
