import math

while True:

    try:
        n = float(input("Inserire valore: "))
        break

    except ValueError:
        print("ERRORE: Inserire valore numerico")

print(f"Il valore approssimato e': {math.ceil(n)}")