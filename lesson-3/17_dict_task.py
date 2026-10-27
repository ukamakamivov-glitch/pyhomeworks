# Ichki valueni olish. Ichma-ich dictionary berilgan. Ichki dictionarylardan biridagi valueni oling.



dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :{'v':8 , 'n':"salom"},
    'k':3
}

for va in dic.values():
    if isinstance(va,dict):
        print(va['n'])
        break

#
# #  Ichki valueni olish. Ichma-ich dictionary berilgan. Ichki dictionarylardan biridagi valueni oling.
#
#
#
#
# dic = {
#     'a':2,
#     'b':3,
#     'c':4,
#      3 :{'v':8 , 'n':"salom",'z':89},
#     'k':3
# }
#
# for k in dic.values():
#     if isinstance(k, dict):
#         for n in k.values():
#             print(n)
#             break
#         break
# else:
#     print("ichki dict mavjud emad")
#
#
