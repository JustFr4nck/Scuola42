ar = [3, 20, 30, 40, 50]
print(ar)

ar2 = []

for x in ar:
    if x > 5:
        ar2.append(x + 2)
    else:
        ar2.append(x)

print(ar2)