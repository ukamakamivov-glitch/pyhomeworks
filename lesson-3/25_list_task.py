# O‘rtadagi elementni olish. List berilgan. O‘rtadagi elementni toping. Elementlar soni juft bo‘lsa,
# o‘rtadagi ikkita elementni qaytaring.


ls = ['ukam','singlim','akam','otam','ukam','otam','onam']
# list elementlari top  bulganda
m = len(ls) // 2

print("O'rtadagi element :", ls[m])
# juft bulgandan elementlar soni

ds = ['ukam','singlim','akam','otam','jaji','otam','onam','baby']

n  = len(ds) // 2

print("O'rtadagi ikkita element :", ds[n-1],",",ds[n])