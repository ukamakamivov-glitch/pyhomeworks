"""
#numerikka berilgan

import math

print(math.sqrt(16)) # ildiz oladigan funksiya math chaqirmasdan ishlamaydi.

c = 3 + 5j #complex son

print(c.real) #real qism
print(c.imag) #mavhum qism
"""
# string intro

# ' - single quote
# " - double quote
# \ - back slash (escape charakter)
# / - forward slash
# \n - newline charakter satr tashlaydi va uni bitta charak hisobiga utadi
# \' - single quote tring ichida
# \" - double quote string ichida
# \t - tab
# \\ - backslash string ichida backslash ishlatish uchun
# \b - back space bitta charakterni oldidan uchiradi


hi = "python k\nundal\nigi"
hi1 = "python k\\nundal\\nigi"
word = 'I\' am teacher'
#print(word)
print(hi1)

directorry = "C:\\Users\\Lider Bro\\Downloads\\AyuGram Desktop"
directorry1 = r"C:\Users\Lider Bro\Downloads\AyuGram Desktop"# row string ichidagi slash va charakterlarnmi uqimaydi
#print(type(directorry))
#print(directorry1)

# string simple app py

# + stringlar uchun "concatenation " dedb nomlanadi


name  = "John" # input("What is your name ?")
age = 30 # int(input("Age : "))
#print("Your name is "+ name +" and you are " + str(age) + " years old.")
#print(f"Your name is {name} and you are {age} years old.") # f string
#print("Your name is {fname} and you are {Age} years old.".format(fname = name,Age = age)) # formating string
#print("Your name is {} and you are {} years old.".format(name, age)) # formating string


"""n = 45.2374862
print(f"{n:.3f}")
print(f"{n=}")
"""

"""name = "John"
name1 = "Kamomoliv"

print(f"{name:<9} - first name") #berilgan raqam stingni boshidan ochirigacha berilgan chrakter miqsori
print(f"{name1:<9} - second name")
"""
my_str = "Hallo salom" # sequence
#print(len(my_str))# str uzunligini charadi

#slicing
#print(my_str[2:5])
print(my_str[:])# obshi hammasini oladi
print(my_str[0:11]) # bu ham hamma strni oladi
print(my_str[::2]) # 2 ta chrakter tashlab strdan olib chiqaradi
#negativ indexlarda ham buladi

print(my_str[-10:-1])

#last characterni topishda

"""word = input("Enter a word: ")
last_charakter = word[-1]
print(f"Last character: {last_charakter}")

"""

# SyntaxError
# TypeError
# ValueError
# IndexError : string index out of range


#Mutable vs Immutable (uzgaruvchan vs uzagarmas)
"""
my_str = "Orange"
print("Oldin :", id(my_str))

my_str = "o" + my_str[1:]
print("Keyin :",id(my_str))

print(my_str)"""



