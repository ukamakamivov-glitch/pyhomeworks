ls = ['olma', 'anor', 'banan', 'nok', 'shaftoli', 'uzum']

# for dan gfoydalanmagan yuli
n = 2
new_ls = []

"""new_ls.append(ls[:n])
new_ls.append(ls[n:4])
new_ls.append(ls[4:])

print(new_ls)"""

# for bilan

for i in range(0, len(ls), n):
    new_ls.append(ls[i:i+n])

print(new_ls)