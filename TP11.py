# Exercice 1 :
def nombre_de_mots(phrase):
    result = 1
    for i in phrase:
        if i == ' ':
            result += 1
        elif i == '!' or i == '?':
            result -= 1
    return result

print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est séparé !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
# Exercice 2 :

class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                arbre.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None:
                arbre.droite.inserer(cle)
            else:
                self.droit = Noeud(cle) 


arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

print(arbre.gauche.etiquette)
print(arbre.droit.etiquette)
print(arbre.gauche.gauche.etiquette)
print(arbre.gauche.droit.etiquette)
