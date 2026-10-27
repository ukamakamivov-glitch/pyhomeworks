# Valuening takrorlanishlar sonini topish. Dictionary berilgan. Muayyan value turli keylar bo‘yicha
# jami necha marta uchrashini sanang.


dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :2,
    'k':3
}

n = 3
k = 0
for i in dic.values():
    if i == n:
     k+=1

print("uchragan : ",k)
