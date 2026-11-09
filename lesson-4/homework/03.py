# input: hello
# output: hel_lo
"""
# birinchi xato kod qilindi

txt = "abcabcdabcdeabcdefabcdefg"
vowels = "aeiou"
result = ""
count = 0
san = set()

for i in range(len(txt)):
    oxirgi = txt[i]
    result = result + oxirgi
    count += 1

    if count >= 3:
        san.add(oxirgi)
        if oxirgi not in vowels and i != len(txt)-1 and oxirgi not in san:
            result += "_"
            san.add(oxirgi)
            count = 0

print(result)
"""

txt = "abcabcdabcdeabcdefabcdefg"
vowels = "aeiou"
result = ""
count = 0
san = set()

for i in range(len(txt)):
    oxirgi = txt[i]
    result += oxirgi
    count += 1

    # Agar 3 ta belgi to'lsa yoki oldingi shart tufayli sanagich oshgan bo'lsa
    if count >= 3:
        # Agar bu harf oldin chiziqcha olgan bo'lsa, uni qayta chiziqchalamaymiz
        if oxirgi in san:
            continue

        # Agar oxirgi harf bo'lsa, chiziqcha qo'yilmaydi
        if i == len(txt) - 1:
            break

        # Agar belgi unli harf bo'lsa yoki uning o'zi/oldingi belgilar shartga tushsa
        if oxirgi in vowels:
            # Unli bo'lsa chiziqchani keyingisiga suramiz, shuning uchun hozir qo'ymaymiz
            continue
        else:
            result += "_"
            san.add(oxirgi)
            count = 0

print(result)

