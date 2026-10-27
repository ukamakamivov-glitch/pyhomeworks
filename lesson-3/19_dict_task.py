# Unique valuelarni sanash. Dictionary berilgan. Unda nechta unique value borligini aniqlang.


dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :0,
    'k':3,
    's':3
}
# uzun qilib tashlaganman :)

a = len(dic.values())
b = len(set(dic.values()))
print("unique valuelar soni :", a-(a - b))


# qisqa

print("Unique valuelar :", len(set(dic.values())))

