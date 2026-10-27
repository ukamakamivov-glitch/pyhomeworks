#  Listlardan dictionary yaratish. Ikkita list (biri keylardan, biri valuelardan iborat) berilgan. Ularni
# juftlab dictionary yarating.


ls = ['s','b',True]
ls_v = [1,2,0]

dic = {}

"""
for key in range(0,len(ls)):
  for v in range(0,len(ls_v)):
      dic[ls[key]] = ls_v[v]

print(dic)
"""

# har qanaqasiga qildim endi zip() ni qilib kuriladi

for key , value in zip(ls,ls_v):
    dic[key] = value

print(dic)

# zip() siz qilsak range() orqali qisa bular ekan

for i in range(min(len(ls),len(ls_v))): # min juftlangaana faaqat 2 ta elemnt bulaa oladi shunda
    dic[ls[i]] = ls_v[i]

print(dic)