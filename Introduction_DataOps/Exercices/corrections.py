
"""
Soit la chaîne de caractères suivante : "mississippi". 
Comptez le nombre d'occurence de chaque lettre(s).
"""

CONTENT="mississippi"

dico={
    char : CONTENT.count(char)
    for char in set(CONTENT)
}

print(dico)


# entier signé ou non inversé -6523 donnerait -3256

NUMBER = -6523

result = int(str(NUMBER)[::-1]) if NUMBER >= 0 else -int(str(-NUMBER)[::-1])
