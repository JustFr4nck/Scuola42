women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(list):

    for x,y in list.items():
       
        item = ""

        for z,c in y.items():
           
           item += str(c) + " "

        print(f"{item[:-5]} is a great scientist born in {item[-5:]} ")   



famous_births(women_scientists)