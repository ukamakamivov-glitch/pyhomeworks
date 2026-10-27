# Tartibni saqlagan holda unique elementlarni olish. List berilgan. Asl tartibni saqlagan holda faqat
# unique elementlardan iborat yangi list yarating.


ls = [4, 2, 7, 4, 2, 9, 7, 5]

ln = set(ls) # for ishlatmaganda

print(list(ln))

ln2 = []
for i in ls:
    if i not in ln2:
         ln2.append(i)

print(ln2)