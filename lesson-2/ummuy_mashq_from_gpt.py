
gap = input("Gap kiritng :") #Salom Python 2026


a  = gap.split()
print("Suzlar soni :",len(a))
unlilar = "auioe"
n = 0
m = 0
for i in gap:
    if i.lower() in unlilar:
        n +=1
    if i.isdigit():
        m += 1
print("Unli harflar :",n)
print("Raqam mavjud:",m>0)
print("Teskari gap:",gap[::-1])
print("Palindrom :",gap[::-1].lower()==gap.lower())