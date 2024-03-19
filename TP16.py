#Exercice 1 :
def ecriture_binaire_entier_positif(n):
    if n == 0:
        return '0'
    else:
        r = n % 2
        q = n // 2
        result = ''
        while q != 0:
            result = str(r) + result
            r = q % 2
            q = q // 2
        return str(r) + result
    
print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))

#
#
#Exercice 2 :

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab.copy()
    tab[i] = temp[j] 
    tab[j] = temp[i] 

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n): 
        for j in range(n): 
            if tab[j] > tab[i]: 
                echange(tab, j, i) 

tab = []
tri_bulles(tab)
print(tab)

tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
print(tab2)

tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
print(tab3)