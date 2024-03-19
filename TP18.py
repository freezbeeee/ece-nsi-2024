#Exercice 1 :
def multiplication(n1, n2):
    result = 0
    for i in range(abs(n1)):
        if n1 > 0:
            result += n2
        else:
            result -= n2
    return result

print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))

#
#
#Exercice 2 :
def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, m , j) 
    elif tab[m] > x:
        return chercher(tab, x, i , m) 
    else:
        return m

#print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
#print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))