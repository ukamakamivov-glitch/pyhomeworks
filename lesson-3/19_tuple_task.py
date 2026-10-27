#  Qiymati bo‘yicha elementni olib tashlash. Tuple va element berilgan. Shu elementning birinchi
# uchrashganini olib tashlagan yangi tuple yarating.


tp = ('a','b','c',3,1,0,3,'a')

ls = list(tp)

ls.remove('a')
new_tuple = tuple(ls)
print(new_tuple)