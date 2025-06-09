while True:

    try:
        first = int(input("Inserire Primo valore: "))
        second = int(input("Inserire secondo valore: "))
        break

    except ValueError:
        print("ERRORE: Inserire valore numerico")
    
print("Grazie!!!")

print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
print(f"{first} X {second} = {first * second}")
print(f"{first} / {second} = {(first / second):.1f}")