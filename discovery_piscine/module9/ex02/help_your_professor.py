class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

def average(classe):

    somma = 0
    inc = 0

    for x,y in classe.items():

        somma += y
        inc += 1

    media = somma / inc

    return media

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
