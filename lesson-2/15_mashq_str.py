#Foydalanuvchidan gap so‘rab, har bir so‘zning birinchi harfidan qisqartma (akronim) yasang.
#Masalan: «World Health Organization» → «WHO».


a = input("Gap yozing :")

suzlar  = a.split()

"""print("Qisqartma : ", end ="") #birinchi variant
for i in suzlar:
    i = i.capitalize()
    print(i[0] , end="")"""
print("Qisqartma : ", end ="")
for i in suzlar:
    print(i[0].upper() , end="")