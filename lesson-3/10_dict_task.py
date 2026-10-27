#  Key-value juftligini olish. Dictionary va key berilgan. Agar key mavjud bo‘lsa, unga tegishli
# key-value juftligini oling.



dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :2
}

n = 'c'

if n in dic:
    n_key = {n:dic[n]}
    print(n_key)
else:
    print("Mavjud emas bunday key")