ar = [3, 20, 30, 20, 50]
print(ar)

ar2 = []

for x in ar:
    if x > 5:
        ar2.append(x + 2)
    else:
        ar2.append(x)

ar2 = set(ar2)
print(ar2)