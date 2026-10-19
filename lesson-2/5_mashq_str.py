"""matn = input("Text kiriting : ")
# for nima qanday ishlashini tushunish uchun
a_soni = 0
matn = matn.lower()
for x in matn:
    if x == "a":
        a_soni += 1
print("a harfi :",a_soni,"qatnashgan")"""

# Berilgan satrdagi unli va undosh harflar sonini hisoblaydigan dastur yozing.

matn = input("Text kiriting : ")

matn = matn.lower()


unlilar = "aiueo"
unli = 0
undosh = 0

for x in matn: # matnni mayadalab x ga miqdor quyib beryapti
    if x in unlilar: # unlilar tekshirib true bulsa unli ga bir qiiymat beryapti
        unli += 1
    elif x.isalpha(): # if false bulganda elif ga kelib tushyapti "132@#!" raqam va charakter busa isalpha() tekshirib false qilyati harf bulganini esa true berib undosh ga 1 qiymat bermoqda
        undosh += 1


print("Unlilar : ", unli)
print("Undoshlar : ", undosh)