#  Dictionaryni key bo‘yicha saralash. Keylar bo‘yicha saralangan yangi dictionary yarating.


dic = {
    'c':3,
    'd':2,
    'a':1,

}

sew_dic = sorted(dic.keys())
new_dic = {}


for k in sew_dic:
    new_dic[k] = dic[k]

print("eski :",dic)
print("yangi :",new_dic)
