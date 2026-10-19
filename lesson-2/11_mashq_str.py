#Satr tarkibida biror raqam bor-yo‘qligini tekshiradigan dastur yozing.

#

gap = input("Gap kiriting : ")
raqamlar = "0123456789"
n = 0
for x in gap:
    if x in raqamlar:
        n += 1 #

#print("Gapda :", n, " raqam qatnashgan")  nechta qatnashganligi
if n > 0 :
    print("Raqam qatnashgan.")
else:
    print("Raqam qatnashmagan.")