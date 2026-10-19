"""
Foydalanuvchidan satr va bitta belgi so‘rang, so‘ng satrdagi shu belgining barcha uchrashlarini
olib tashlang.

"""


a = input("Satr kirit :")
b = input("Belgi kirit :")

# for , if , in orqali ishlangan usuli
print("Natija :", end = "")
for x in a:
    if x  not in b:
        print(x, end="")

print(" ")
print("Natija - 2:", a.replace(b, "")) # replace() methoda bitta qator qisa bular edi



