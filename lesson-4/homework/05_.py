pas = input("Parol kiriting :")


if  not (len(pas) >= 8):
    print("Password is too short.")

elif not any(x.isupper() for x in pas):
    print("Password must contain anuppercase letter.")
else:
    print("Password is strong.")

