a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
c = int(input("Uchunchi son: "))

"""if a > b and a > c :
    print(f"Eng katta son Birinchi son : {a}")
elif a == b == c:
    print("Uchala son ham teng")
elif b > a and b > c :
    print(f"Eng katta son Ikkinchi son : {b}")
elif c> a and c > b :
    print(f"Eng katta son Uchinchi son : {c}")
elif a == c :
    print("Eng katta son Birinchi son va Uchinchi son")
elif a == b :
    print("Eng katta son Birinchi son va Ikkinchi son")
elif c == b :
    print("Eng katta son Ikkinchi son va Uchinchi son")

if a < b and a < c :
    print(f"Eng Kichik son Birinchi son : {a}")
elif b < a and b < c :
    print(f"Eng Kichik son Ikkinchi son : {b}")
elif c< a and c < b :
    print(f"Eng Kichik son Uchinchi son : {c}")
elif a == b == c:
    print("Eng katta va eng kichik son teng")
elif a == c :
    print("Eng Kichik son Birinchi son va Uchinchi son")
elif a == b :
    print("Eng Kichik son Birinchi son va Ikkinchi son")
elif c == b :
    print("Eng Kichik son Ikkinchi son va Uchinchi son")"""


max_num = max(a, b, c)
min_num = min(a, b, c)
if max_num == min_num:
    print("Eng katta son eng kichik songa  teng")
else:
    print("Eng katta son :",max_num)
    print("Eng kichik son :",min_num)