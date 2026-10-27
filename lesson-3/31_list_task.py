ls = [10, 20, 30]
n = 2
"""ln = sorted(ls * 2)
print(sorted(ln))"""

# for da bulagnda

ln = []

for x in ls:
    ln.extend([x] * n)

print(sorted(ln))