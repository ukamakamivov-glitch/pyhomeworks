 #Berilgan satr palindrom ekanligini tekshiradigan Python dasturi yozing.

palindrom = input("Text kiriting : ")
x = palindrom.lower() #qushimcha qushdim kichik kattta faqr qilmay tekshiradi
if x[::-1] == x:
    print("Text palindrom ekan")
else:
    print("Text palindrom emas")