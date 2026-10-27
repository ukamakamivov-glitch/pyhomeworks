#  Takroriy elementlarni olib tashlash. List berilgan. Asl listdagi faqat takrorlanmaydigan (unique)
# elementlarni o‘z ichiga olgan yangi list yarating.

ls = ['ukam','singlim','akam','otam','ukam','otam','onam']

new_ls = set(ls)
print(list(new_ls))
