dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_redheads(dupont_family):

    ar = []

    for x,y in dupont_family.items():

        if y == "red":

            ar.append(x)
        
    return ar

print(find_the_redheads(dupont_family))