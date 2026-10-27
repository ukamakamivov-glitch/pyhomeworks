# Ikkinchi eng kichik element. Berilgan tuple ichidagi ikkinchi eng kichik elementni toping.


tp = (3,2,5,4,5,2,0)

mi = min(tp)

sp = []

for i in range(0,len(tp)):
    if tp[i] > mi:
        sp.append(tp[i])

print("eng kichik ikkchi son:",min(sp))