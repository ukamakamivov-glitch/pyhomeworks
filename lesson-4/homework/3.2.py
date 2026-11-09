"""
Har 3-harfdan keyin yulduzcha (*) qo'yilishi kerak.
Lekin shu 3 ta harflik guruh (blok) ichida bir xil harf takrorlangan bo'lsa (masalan, aba yoki add),
 yulduzcha qo'yilmaydi va sanoq keyingi harfdan yangidan (0 dan) boshlanadi.

"""

txt = "aaabccdef"

result = ""
block = ""

for i in range(len(txt)):
    last = txt[i]
    result += last
    block  += last

    if len(block) == 3:
        if len(set(block)) != 3 and i != len(txt)-1 and len(set(block)) != 1:
            result += "*"

        block = ""


print(result)
