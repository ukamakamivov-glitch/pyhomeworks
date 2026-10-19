from datetime import datetime

yil = datetime.now().year

ism = input("Ismingiz : ")
yili = int(input("Tug'ilgan yillingiz : "))

yosh = yil - yili

print(ism ,f"sizning yoshingiz : {yosh}")