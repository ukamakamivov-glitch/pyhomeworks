
# bu faqat 1 dan  100 gacha ishlaaydi

"""for i in range(1,100):

    if i > 1 and i % 2 != 0 and i % 3 !=0 and i % 5 != 0 and i % 7 != 0 or i == 2 or i == 3 or i == 5 or i == 7:
        print(i, end=" ")
"""



# nested loop da ishlatish kerak

"""for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            # i soni tub emas
            break
    else:
        print(i, end=" ")
        """

# while orqali ishlash buni gpt dan suralgan

i = 2

while i <= 100:
    j = 2
    is_prime = True

    while j < i:
        if i % j == 0:
            is_prime = False
            break
        j += 1

    if is_prime:
        print(i, end=" ")

    i += 1