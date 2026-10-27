# Dictionaryni teskari qilish. Dictionary berilgan. Keylar va valuelarning o‘rnini almashtirgan yangi
# dictionary yarating.

dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :2,
    'k':0
}
new_dic = {}
for key, value in dic.items():
     new_dic[value] = key


print(new_dic)
