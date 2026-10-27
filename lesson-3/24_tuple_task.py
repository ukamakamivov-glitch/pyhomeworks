#  Unique elementlarni olish. Tuple berilgan. Asl tartibni saqlagan holda faqat unique elementlardan
# iborat yangi tuple yarating.

tp = ('l','e','v','e','l',23,0,1,2,3,2,1,5,23)

# dict usullida
tp_new = tuple(dict.fromkeys(tp)) #set tartibni buzibb yubboradi
print(tp_new)
# for da qilindi
tp2 = []
for i in tp:
    if i not in tp2:
       tp2.append(i)

print(tuple(tp2))