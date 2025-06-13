class Phonebook:


    phonebook = {}

  
    def __init__(self):
        pass

    def add_contact():

        while True:
            try:
                number = str(input("Inserisci il numero di telefono: "))
                break
            except ValueError:
                print("This isn't a valid number.")
        while True:
            try:
                name = str(input("Inserisci il nome: "))
                break
            except ValueError:
                print("This isn't a valid name.")
        Phonebook.phonebook.update({name: number})



    def remove_contact():
        
        while True:
            
            try:
                number = str(input("Inserisci il numero di telefono: "))
                break
            except ValueError:
                print("Valore non valido")

        for x,y in Phonebook.phonebook.items():

            if y == number:

                Phonebook.phonebook.pop(x)
                print("Rimozione effettuata")
                return
        print("Numero non trovato")


                
        



    def contact_list():

        if not Phonebook.phonebook:
            print("La rubrica è vuota.")
            return
        for name, number in Phonebook.phonebook.items():
            print(f"Nome: {name}, Numero: {number}")
    

class Main:
     
    ext = True
    while ext:

    
        cmd = str(input("Cosa vuoi fare (ADD, REMOVE, LIST, CLOSE): "))
    
        match cmd:
            
            case "ADD":
                Phonebook.add_contact()
            case "REMOVE":
                Phonebook.remove_contact()
            case "LIST":
                Phonebook.contact_list()
            case "CLOSE":
                print("Chiusura del programma...")
                ext = False