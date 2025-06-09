import time

n = 100

while n >= 25:

    try:
        n = int(input("Inserire un valore numerico inferiore di 25: "))
        if n >= 25:
            print("ERRORE: inserire valore inferiore a 25")
    except ValueError:
        print("ERRORE: Inserire valore numerico")



while n <= 25:

    print(f"loop variable: {n}")
    n += 1
    time.sleep(1)

