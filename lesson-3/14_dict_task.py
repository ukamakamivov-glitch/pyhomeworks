# Value bo‘yicha keylarni topish. Dictionary va value berilgan. Shu valuega ega barcha keylardan list
# yarating

dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :2,
    'k':3
}
nn = []
n = 3
for key, value in dic.items():
     if n == dic[key]:
      nn.append(key)

print(nn)
