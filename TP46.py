#Exercice 1 :
def recherche(tab, x):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if tab[m] == x:
            return m
        elif tab[m] < x:
            debut = m + 1
        else:
            fin = m - 1
    return None

print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#Exercice 2 : 
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c 
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))