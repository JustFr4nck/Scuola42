import time

while True:

    try:
        n = int(input("Inserire un valore numerico: "))
        break

    except ValueError:
        print("ERRORE: Inserire valore numerico")


for x in range(10):
   
    result = x * n
    print(f"{x} X {n} = {result}")
    time.sleep(1)

