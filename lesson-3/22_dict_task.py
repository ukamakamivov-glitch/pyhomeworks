# Value bo‘yicha filtrlash. Dictionary berilgan. Faqat ma’lum bir shartga mos keladigan valuega ega
# elementlarni o‘z ichiga olgan yangi dictionary yarating.

dic = {
    'c':3,
    'd':2,
    'a':1,
    'b':8,
    't':10

}

new_sort = filter(lambda x:x % 2==0, dic.values() ) # faaaqat juft sonli valulerni oladigan

new_dic = {}

for n in new_sort:
    for k in dic.keys():
        if dic[k] == n:
            new_dic[k] = n


print(new_dic)

