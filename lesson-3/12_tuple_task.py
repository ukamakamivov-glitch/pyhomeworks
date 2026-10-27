#  Ikkinchi eng katta element. Berilgan tuple ichidagi ikkinchi eng katta elementni toping.


tp = (3,2,5,4,5,2,0)

mx = max(tp)
ts = []


for x in tp:
    if x < mx:
        ts.append(x)

print("ikkinchi katta son :",max(ts))