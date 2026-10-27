# Ichma-ich dictionarylarni tekshirish. Dictionary berilgan. Uning valuelari orasida yana dictionary
# bo‘lganlari bor yoki yo‘qligini tekshiring.


dic = {
    'a':2,
    'b':3,
    'c':4,
     3 :{'v':8},
    'k':3
}
n = 0
for va in dic.values():
    if type(va) == type(dict()): # type(va) == dict qisaa ham bulara edi ;)
        print("Ha bor")
        break
else: print("yuq")

# 2   - usul

for va in dic.values():
    if isinstance(va,dict): # bu type larni tekshiradigan maxsus funksiya
        print("Ha bor")
        break
else: print("yuq")