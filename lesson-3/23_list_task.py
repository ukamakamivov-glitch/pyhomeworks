# Toq sonlarni filtrlash. Butun sonlardan iborat list berilgan. Faqat toq sonlarni o‘z ichiga olgan yangi
# list yarating.


ls = [1,4,2,23,6,12,6,1,4,23,3]

ts = list(filter(lambda x : x % 2 !=0,ls))

print(ts)