"""Foydalanuvchidan gap va almashtiriladigan so‘zni so‘rang. Ushbu so‘zni foydalanuvchi kiritgan
boshqa so‘z bilan almashtiring. Masalan: «I love apples.» → «apples» o‘rniga «oranges» → «I love
oranges.»"""


a = input("Gap  kiring : ")
c = input("O'zgartiriladigan suzni kiriting : ")



b = input(f"{c} ni urniga qaysi suzni almashtirasiz : ")
print("Kiritgan yangi suzingiz :", b)
print("Natija : ", end = "")
print(a.replace(c, b))

