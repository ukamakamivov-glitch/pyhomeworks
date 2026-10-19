# Satr ma’lum bir so‘z bilan boshlanishini va boshqa bir so‘z bilan tugashini tekshiradigan dastur
# yozing. Masalan: «Python is fun!»; boshlanishi: «Python»; tugashi: «fun!».

#bu ishlagani xato ekan notugri tushundim
"""strs = input("text kiriting : ")

a = strs.split()
b = a[0]
c = a[-1]

if bool(b):
    print("Satr boshi :",b)
if bool(c):
    print("Satr oxiri :",c)
else:
    print("False")"""



txt = input("text kiriting : ")
satr1 = input("boshlanish suz :")
satr2 = input("oxirgi suz :")

print(txt.startswith(satr1) and  txt.endswith(satr2))

