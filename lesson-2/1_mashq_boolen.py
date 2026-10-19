#Foydalanuvchi nomi va parolni qabul qilib, ikkalasi ham bo‘sh emasligini tekshiradigan dastur
#yozing.


a = input("Foydaalanuvchi nomi :")
b = input("Parol :")
a = a.replace(" ", "")

b = b.replace(" ", "")

print("Foydalanuvhichi :",bool(a))
print("Parol :",bool(b))