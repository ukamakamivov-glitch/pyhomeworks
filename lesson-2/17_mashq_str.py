#  Foydalanuvchidan satr so‘rab, undagi barcha unli harflarni biror belgi (masalan, «*») bilan
# almashtiring.
txt = input("text yozing : ")

unlilar = "auioe"

#txt = txt.lower()

for i in txt:
    if i.lower() not in unlilar: #lower() ichida berib ketsa buladi
        print(i, end="")
    else:
        print("*",end = "")

