n = -1

while n < 0:

    try:
        n = int(input("Inserire la tua eta': "))

    except ValueError:
        print("ERRORE: Inserire valore numerico")
    
    if n < 0:
        print("ERRORE: non puoi avere meno di 0 anni")

print(f"Fra 10 anni, avrai {n + 10} anni")
print(f"Fra 20 anni, avrai {n + 20} anni")
print(f"Fra 30 anni, avrai {n + 30} anni")