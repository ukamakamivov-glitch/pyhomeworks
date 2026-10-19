#So‘zlar ro‘yxatini qabul qilib, ularni ma’lum bir belgi (masalan, «-» yoki «,») bilan ajratilgan
#yagona satrga birlashtiradigan dastur yozing.

a = input("Suzlar kiriting : ")

suzlar = a.split()
print("Suzlar : ", suzlar)


c ="-".join(suzlar)
print("Birlashtirilgan suzlar : ", c)


