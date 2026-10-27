# Juft sonlarni filtrlash. Butun sonlardan iborat list berilgan. Faqat juft sonlarni o‘z ichiga olgan yangi
# list yarating.

ls = [1,4,2,23,6,12,6,1,4,23]

jl = list(filter(lambda x : x % 2 ==0,ls))\

#jl = ls.copy()

print(jl)