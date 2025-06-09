
while True:

    try:
        n = float(input("Inserire valore: "))
        break

    except ValueError:
        print("ERRORE: Inserire valore numerico")

f = int(n)

n -= f

if n == 0:
    print("Il valore e' intero")

else:
    print("Il valore e' decimale")