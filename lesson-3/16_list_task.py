  #   Toq sonlarni sanash. Butun sonlardan iborat list berilgan. Undagi toq sonlar nechta ekanini sanang.


ls = [1,2,3,4,54,1,2,3,6,4,8]

toq_son = list(filter(lambda x : x % 2 != 0, ls))

print("Toq sonlar : ", len(toq_son))