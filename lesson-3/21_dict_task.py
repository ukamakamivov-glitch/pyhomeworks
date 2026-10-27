# Dictionaryni value bo‘yicha saralash. Valuelar bo‘yicha saralangan yangi dictionary yarating.


dic = {
    'c':3,
    'd':2,
    'a':1,

}

new_sort = sorted(dic.values())

new_dic = {}

for n in new_sort:
    for k in dic.keys():
        if dic[k] == n:
            new_dic[k] = n


print(new_dic)







