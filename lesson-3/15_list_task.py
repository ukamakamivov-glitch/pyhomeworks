# Juft sonlarni sanash. Butun sonlardan iborat list berilgan. Undagi juft sonlar nechta ekanini sanang.


ls = [1,2,3,4,54,1,2,3,6,4,8]

juft = list(filter(lambda x : x % 2 == 0, ls))

print(juft)
print("juft sonlar :", len(juft))