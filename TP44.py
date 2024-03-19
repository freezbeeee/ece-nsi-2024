#Exercice 1 :
def enumere(tab):
    result = {}
    for n in range(len(tab)):
        r = []
        for i in range(len(tab)):
            if tab[i] == tab[n]:
                r.append(i)
        result[tab[n]] = r
    return result

print(enumere([]))
print(enumere([1, 2, 3]))
print(enumere([1, 1, 2, 3, 2, 1]))

#
#
#Exercice 2 :
"""
class Noeud:
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if arbre.gauche == None: 
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle) 
        return arbre
"""