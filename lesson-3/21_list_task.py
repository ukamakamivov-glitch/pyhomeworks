# Ikkinchi eng kichik element. Berilgan listdagi ikkinchi eng kichik elementni toping.


ls = [1,4,2,23,6,12,6,1,6,4,23]

mn = min(ls) # eng kichik son

ls = list(filter(lambda x:x != mn,ls))

min2 = min(ls)
print("Eng kichik ikkinchi son :",min2)
