word = ""

while not word.isalpha(): 
    word = input("Inserisci la parola: ")

    if not word.isalpha():
        print("ERRORE: inserire solo caratteri testuali")

print(f"Parola in maiuscolo: {word.upper()}")