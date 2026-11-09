

txt = '12abcdef'

unli = 'auieo'
rum = "1234567890"
result = ""
count = 0
skip_next = False

for i in range(len(txt)):
    last = txt[i]
    result += last

    if skip_next:
        count = 0
        skip_next = last in rum
        continue

    if last in rum:
        count = 0
        skip_next = True
        continue

    count += 1

    if count >= 3:

        if i == len(txt) - 1:
            break

        if last in unli :
            continue
        else:
            result += "_"
            count = 0

print(result)

